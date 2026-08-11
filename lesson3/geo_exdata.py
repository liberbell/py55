import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString, Polygon
import geodatasets
from geodatasets import get_path

# print(geodatasets.data)
# pd.set_option('display.max_columns', None)

# df = pd.DataFrame.from_dict(geodatasets.data, orient='index')
# print(df)

data_path = geodatasets.get_path("airbnb")
# data_path = "https://githubusercontent.com"
# data_path = "https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zip"

# gdf1 = gpd.read_file(data_path)


# print(gdf1)