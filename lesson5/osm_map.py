import folium
import osmnx as ox
import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString, Polygon

# query = "Kamakura-shi, Kanagawa, Japan"
query = "sumida, Tokyo, Japan"
G = ox.graph_from_place(query, network_type="drive")


# m = ox.plot_graph_folium(G, tiles="OpenStreetMap", color="blue", weight=2)

gdf_nodes, gdf_edges = ox.graph_to_gdfs(G)
center_lat = gdf_nodes["y"].mean()
center_lng = gdf_nodes["x"].mean()

m = folium.Map(location=[center_lat, center_lng], zoom_start=12, tiles="OpenStreetMap")

# folium.GeoJson(
#     gdf_edges,
#     style_function=lambda feature: {
#         "color": "blue",
#         "weight": 2,
#         "opacity": 0.7
#     }
# ).add_to(m)

gdf1 = ox.graph_to_gdfs(G)[0]
# print(gdf1)

gdf2 = ox.graph_to_gdfs(G)[1]
# print(gdf2)

skytree = (35.7100, 139.8108)
skytree_x = 139.8093
skytree_y = 35.7090
edo_museum = (35.6963, 139.7967)
edo_museum_x = 139.7944
edo_museum_y = 35.6961

start = ox.nearest_nodes(G, X=skytree_x, Y=skytree_y)
end = ox.nearest_nodes(G, X=edo_museum_x, Y=edo_museum_y)

print(f"始点ノードID: {start}")
print(f"終点ノードID: {end}")

shortest_path = ox.shortest_path(G, start, end)

route_gdf = ox.routing.route_to_gdf(G, shortest_path)
# m = folium.Map(location=[skytree_y, skytree_x], zoom_start=14)

folium.GeoJson(
    route_gdf,
    style_function=lambda x: {
        "color": "blue",
        "weight": 5,
        "opacity": 0.8,
    },
).add_to(m)

folium.Marker(
    location=[skytree_y, skytree_x],
    tooltip="start",
    icon=folium.Icon(color="red"),
).add_to(m)

folium.Marker(
    location=[edo_museum_y, edo_museum_x],
    tooltip="end",
    icon=folium.Icon(color="red"),
).add_to(m)

# new_fmap = ox.plot_route_folium()

m.save("route_from_skytree.html")