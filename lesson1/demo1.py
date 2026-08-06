import geopandas as gpd
import folium
import matplotlib.pyplot as plt
from geodatasets import get_path

path = get_path("nybb")
gdf = gpd.read_file(path)

print(gdf.head())

gdf.plot()
plt.show()