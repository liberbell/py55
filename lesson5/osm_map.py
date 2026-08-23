import folium
import osmnx as ox
import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString, Polygon

query = "Yokohama-shi, Kanagawa, Japan"
G = ox.graph_from_place(query, network_type="drive")