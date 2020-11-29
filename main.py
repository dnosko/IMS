import geopandas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import contextily as ctx
import logging
from shapely.geometry import LineString

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

# EPSG:30177 or 900913 ??
# df = df.to_crs("epsg:900913")

areas = ['Japan', 'Mexico']
original_file = '{}.geojson'
cleaned_file = '{}_cleaned.geojson'


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

    #simplify lines
    orig_df['geometry'] = orig_df.simplify(0.0008)

    # desired area only
    df_bounds = orig_df['geometry'].bounds
    df_concat = pd.concat([orig_df, df_bounds], axis=1, sort=False)
    filtered_df = df_concat[(df_concat['maxx'] < 140.074313) & (df_concat['minx'] > 132.120212)
                            & (df_concat['maxy'] < 41.169922) & (df_concat['miny'] > 35.065470)
                            & ((df_concat['maxx'] < 136.7) | (df_concat['maxy'] > 36))]

    # save result
    filtered_df.to_file(cleaned_file.format(area), driver='GeoJSON')

    return filtered_df


if __name__ == "__main__":
    df = geopandas.read_file(cleaned_file.format('Japan'))

    fig, ax = plt.subplots(1, 1, figsize=(20, 15))
    df.plot(ax=ax, linewidth=3)
    plt.show()
