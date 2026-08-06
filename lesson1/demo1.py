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

m = folium.Map(location=[40.7, -73.94], zoom_start=10, tiles="CartoDB positron")

for _, r in gdf.itterrows():
    sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
    geo_j = sim_geo.to_json()
    geo_j = folium.GeoJson(data=geo_j, style_function=lambda x: {"fillcolor": "orange"})
    folium.Popup(r["BoroName"]).add_to(geo_j)
    geo_j.add_to(m)

output_file = "map.html"
m.save(output_file)