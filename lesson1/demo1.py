import geopandas as gpd
import folium
import matplotlib.pyplot as plt
from geodatasets import get_path

path = get_path("nybb")
gdf = gpd.read_file(path)

print(gdf.head())

gdf.plot()
# plt.show()

gdf = gdf.to_crs(epsg=4326)
print(gdf.crs)
print(gdf.head())