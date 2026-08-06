import geopandas as gpd
import folium
import matplotlib.pyplot as plt

path = gpd.dataset.get_path("nybb")
gdf = gpd.read_file(path)

print(gdf.head())
