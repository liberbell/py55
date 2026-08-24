import folium
import osmnx as ox
import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString, Polygon

query = "Kamakura-shi, Kanagawa, Japan"
G = ox.graph_from_place(query, network_type="drive")


# m = ox.plot_graph_folium(G, tiles="OpenStreetMap", color="blue", weight=2)

gdf_nodes, gdf_edges = ox.graph_to_gdfs(G)
center_lat = gdf_nodes["y"].mean()
center_lng = gdf_nodes["x"].mean()

m = folium.Map(location=[center_lat, center_lng], zoom_start=12, tiles="OpenStreetMap")

folium.GeoJson(
    gdf_edges,
    style_function=lambda feature: {
        "color": "blue",
        "weight": 2,
        "opacity": 0.7
    }
).add_to(m)

gdf1 = ox.graph_to_gdfs(G)[0]
print(gdf1)

gdf2 = ox.graph_to_gdfs(G)[1]
print(gdf2)

skytree = (35.7100, 139.8108)
edo_museum = (35.6963, 139.7967)

start = ox.nearest_nodes(G, skytree)
end = ox.nearest_nodes(G, edo_museum)



# m.save("kanagawa_road_map.html")