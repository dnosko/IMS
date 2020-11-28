from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

#35.19266414615366, 132.56575702690475
#40.84789071506689, 139.6409525751002
map = Basemap(llcrnrlon=132.56575702690475,llcrnrlat=35.19266414615366,urcrnrlon=139.6409525751002,urcrnrlat=40.84789071506689,
resolution='h')

#map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='green',lake_color='aqua')
map.drawcoastlines()

plt.show()
