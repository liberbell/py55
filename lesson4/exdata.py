import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString, Polygon
import geodatasets
from geodatasets import get_path

# gdf = gpd.read_file("N02-19_GML/N02-19_RailroadSection.shp", encoding="shift-jis")
gdf = gpd.read_file("N02-19_GML/N02-19_RailroadSection.geojson", encoding="utf-8")
# print(gdf)

fig = plt.figure(figsize=(8, 10))
ax = fig.add_subplot(1, 1, 1)

m = gdf.explore(m=ax)
output_file = "train_exdata.html"
m.save(output_file)