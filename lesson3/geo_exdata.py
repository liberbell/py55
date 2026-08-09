import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString, Polygon
import geodatasets

# print(geodatasets.data)

data_path = geodatasets.get_path("naturalearth.lowres")

gdf1 = gpd.read_file(data_path)


print(gdf1)