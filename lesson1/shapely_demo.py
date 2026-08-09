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

# cords = [((0, 0), (1, 1)), ((-1, 0), (1, 0))]
# lines = MultiLineString(cords)

a = Polygon([(0, 0), (0, 1), (1, 1), (1, 0)])
b = Polygon([(2, 0), (2, 1), (3, 1), (3, 0)])
# polygons = MultiPolygon([a, b])

l = LineString([(1, -1), (1, 0), (2, 0), (2, 1)])

gdf = gpd.GeoDataFrame(geometry=[l], crs="EPSG:4326")


m = gdf.explore()
output_file = "shapely_result.html"
m.save(output_file)