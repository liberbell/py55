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

data_path = geodatasets.get_path("geoda.airbnb")
# data_path = "https://githubusercontent.com"
# data_path = "https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zip"


gdf1 = gpd.read_file(data_path)

gdf2 = gpd.read_file(
    "https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/"
    "ne_110m_populated_places_simple.geojson"
)

ax = gdf1.explore()
gdf2.explore(ax=ax, color="orange", marker_kwds={"radius": 3})

output_file = "exdata_result.html"
ax.save(output_file)