import pandas as pd
import geopandas as gpd
import matplotlib as plt
from shapely.geometry import Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon

point = Point(0.0, 1.0)
print(point)

# line = LineString([(0, 0), (1, 1), (3, 0), (5, 2)])

# gdf = gpd.GeoDataFrame(geometry=[line], crs="EPSG:4326")

# polygon = Polygon([(0, 0), (1, 1), (3, 0), (0, 0)])

# points = MultiPoint([(0, 0), (1, 0)])

cords = [((0, 0), (1, 1)), ()]
lines = MultiLineString(cords)

gdf = gpd.GeoDataFrame(geometry=[points], crs="EPSG:4326")


m = gdf.explore()
output_file = "shapely_result.html"
m.save(output_file)