import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString, Polygon
import geodatasets
from geodatasets import get_path

# gdf = gpd.read_file("N02-19_GML/N02-19_RailroadSection.shp", encoding="shift-jis")
gdf = gpd.read_file("N02-19_GML/N02-19_RailroadSection.geojson", encoding="utf-8")
# print(gdf["N02_003"].unique())
# print(gdf)
# print(gdf["路線名"].unique())

gdf_yamanote = gdf[gdf["路線名"]== "山手線"]

# m = gdf.explore(width=500, height=800)
m = gdf_yamanote.explore()
output_file = "train_exdata.html"
m.save(output_file)