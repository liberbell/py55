import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString, Polygon

# d = {"cal1": ["A", "B"], "geometry": [Point(0, 1), Point(1, 0)]}
# gdf = gpd.GeoDataFrame(d)

d = {"cal1": ["A", "B"], "geometry": [LineString([(0, 1), (1, 0)]), LineString([(2, 0), (2, 2)])]}
gdf = gpd.GeoDataFrame(d)

print(gdf, type(gpd))
# gdf = gpd.GeoDataFrame(geometry=[result], crs="EPSG:4326")


m = gdf.explore()
output_file = "gpd_result.html"
m.save(output_file)