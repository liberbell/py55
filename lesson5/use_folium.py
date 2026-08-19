import pandas as pd
import geopandas as gpd
import folium

lat = 35.71
lon = 139.81

map = folium.Map(location=[lat, lon], zoom_start=16)

map.save("tokyo_map.html")