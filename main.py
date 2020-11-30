import geopandas
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import contextily as ctx
import logging
from shapely.geometry import LineString
from shapely.ops import unary_union, transform
import os
import timeit
import sys

"""
(type=boundary and  boundary=administrative and admin_level=2) in "Japan"
area[bbox="34.972041,132.069804,41.166746,140.518291"]->.a;
(natural=coastline and place=island) in "Japan"
"""

"""
area["name:en"="Japan"]->.country;
rel["name:en"="Japan"]["type"="boundary"]["admin_level"="2"];
(
way(r)["maritime" != "yes"](area.country);
way(area.country)["natural"="coastline"](area.country);
);
out geom;
"""

# I would recommend you to use WSG84(EPSG:4326) or Google Mercator(EPSG:900913)
# EPSG:30177 or 900913 ??
# df = df.to_crs("epsg:900913")

data_folder = 'data'

areas = ['Japan', 'Mexico']

original_file = os.path.join(data_folder, '{}.geojson')
cleaned_file = os.path.join(data_folder, '{}_cleaned.geojson')

ca_scale = 5.0
crs = 'EPSG:4326'


def clear_original_dataset(area="Japan"):
    orig_df = None
    file_name = original_file.format(area)
    try:
        orig_df = geopandas.read_file(file_name)
    except OSError or IOError:
        logging.error(f'Can not open file {file_name}')
        exit(1)

    # no Polygons, no rocks no small islands
    orig_df = orig_df[(orig_df['geometry'].type != 'Polygon')
                      & (orig_df['place'] != 'rock')
                      & (orig_df['place'] != 'islet')]
    orig_df = orig_df[['geometry', 'id']]

    # simplify lines => smaller size
    orig_df['geometry'] = orig_df.simplify(0.001)

    # desired area only
    df_bounds = orig_df['geometry'].bounds
    df_concat = pd.concat([orig_df, df_bounds], axis=1, sort=False)
    filtered_df = df_concat[(df_concat['maxx'] < 140.074313) & (df_concat['minx'] > 132.120212)
                            & (df_concat['maxy'] < 41.169922) & (df_concat['miny'] > 35.065470)
                            & ((df_concat['maxx'] < 136.7) | (df_concat['maxy'] > 36))]

    # merge overlapping lines
    multiline_gs = geopandas.GeoSeries(unary_union(filtered_df['geometry']))

    # save result
    multiline_gs.to_file(cleaned_file.format(area), driver='GeoJSON')

    return filtered_df


def get_area_info(bounds):
    max_vals = pd.DataFrame(bounds[['maxx', 'maxy']].max()).transpose()
    min_vals = pd.DataFrame(bounds[['minx', 'miny']].min()).transpose()

    min_max = pd.concat([min_vals, max_vals], axis=1, sort=False)
    shape = (min_max['maxx'] - min_max['minx'], min_max['maxy'] - min_max['miny'])

    return shape, min_max


def transform_deg_to_km(df):
    """
    Latitude: 1 deg = 110.574
    Longtitude: 1 deg = 111.320 * cos(Latitude)
    x` = 111.320 * cos(y) * km
    y` = 110.574 * y km
    """

    def shapely_deg_to_km(x, y, z=None):
        return ((111.320 * np.cos(np.deg2rad(y)) * x) / ca_scale, (110.574 * y) / ca_scale)

    def pandas_deg_to_km(line_string: LineString):
        return transform(shapely_deg_to_km, line_string)

    return df.apply(pandas_deg_to_km)


def cross_cover(points, df):
    bnd = df.buffer(0.5)
    print(sys.getsizeof(bnd))


def lines_to_points(df):
    shape, min_max = get_area_info(df.bounds)
    x = pd.DataFrame(np.arange(0, int(min_max['maxx'].iloc[0])), columns=['x', ])
    y = pd.DataFrame(np.arange(0, int(min_max['maxx'].iloc[0])), columns=['y', ])
    x['key'] = True
    y['key'] = True
    coords_df = pd.merge(x, y, on='key').drop('key', 1)

    points_df = geopandas.GeoDataFrame(coords_df,
                                       geometry=geopandas.points_from_xy(coords_df['x'], coords_df['y']),
                                       crs=crs)

    points = points_df.drop('x', 1).drop('y', 1)
    points = cross_cover(points, df)
    return points


def get_ca_borders(area='Japan'):
    file_name = cleaned_file.format(area)
    if not os.path.isfile(file_name):
        df = clear_original_dataset(area)
    else:
        df = geopandas.read_file(file_name)

    # to real kms
    df.to_crs(crs)

    # move to 0 => minx, miny = 0
    shape, min_max = get_area_info(df.bounds)
    df = df.translate(xoff=-min_max['minx'], yoff=-min_max['miny'])

    # reshape to 1 unit ~= 5km
    df = transform_deg_to_km(df)

    points = lines_to_points(df)
    return points


if __name__ == "__main__":
    df = get_ca_borders('Japan')

    # fig, ax = plt.subplots(1, 1, figsize=(20, 15))
    # df.plot()
    #
    # plt.show()
    # plt.close(fig)
