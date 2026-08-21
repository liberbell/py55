import pandas as pd
import geopandas as gpd
import folium

lat = 35.71
lon = 139.81

map = folium.Map(location=[lat, lon], zoom_start=16)

folium.Marker(
    location=[lat, lon],
    icon=folium.Icon(color="red", icon="camera"),
    popup="Tokyo Sky Tree",
    tooltip="Here"
).add_to(map)

folium.Circle(
    location=[lat, lon],
    radius=100,
    color="blue",
    fill=True,
    fill_opacity=0.5
).add_to(map)

# map = folium.Map(location=[lat, lon], zoom_start=16, tiles="cartodbdark_matter")
# map = folium.Map(location=[lat, lon], zoom_start=16, tiles="stamenterrain")

df = pd.read_csv("data/kindergartenlist.csv", encoding="shift-jis")
print(df)

map.save("tokyo_map.html")