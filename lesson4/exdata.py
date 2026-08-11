import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString, Polygon
import geodatasets
from geodatasets import get_path

gdf = gpd.read_file("N02-19_GML/N02-19_RailroadSection.shp", encoding="shift-jis")
print(gdf)

m = gdf.explore()
output_file = "train_exdata.html"
m.save(output_file)