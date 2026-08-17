import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString, Polygon
import geodatasets
from geodatasets import get_path

pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', None)

# gdf = gpd.read_file("N02-19_GML/N02-19_RailroadSection.shp", encoding="shift-jis")
train_gdf = gpd.read_file("N02-19_GML/N02-19_RailroadSection.geojson", encoding="utf-8")
# print(gdf["N02_003"].unique())
# print(gdf)
# print(gdf["路線名"].unique())

# gdf_yamanote = gdf[(gdf["路線名"]== "山手線") & (gdf["運営会社"] == "東日本旅客鉄道")]
# print(gdf_yamanote)

# df = pd.read_csv("N02-19_GML/kokyoshisetsu.csv", encoding="cp932")
df = pd.read_csv("N02-19_GML/koban.csv", encoding="cp932")
# print(df)

# geometry = gpd.points_from_xy(df["経度"], df["緯度"])
# gdf = gpd.GeoDataFrame(df, geometry=geometry)

gyosei = gpd.read_file("N03-20240101_13_GML/N03-20240101_13.shp")
# print(gyosei)

# gyousei_temp = gyosei.dropna(subset=["N03_004"])
# print(gyousei_temp)

# gyousei_ku = gyosei[gyosei["N03_004"].str.contains("区")]
# print(gyousei_ku)

# pd.DataFrame(gyousei_ku).to_csv("output.csv", index=False)
# a = []
# for index, row in gdf.iterrows():
#     a.append(list(row["geometry"].coords))
# print(a)
# b = gdf.apply(lambda row:list(row.geometry.coords), axis=1)
# print(type(b))
# print(gdf)

# c = gdf.apply(lambda row:list(row.geometry.coords), axis=1)

# ax = gdf.explore()
shinagawa = gyosei[gyosei["N03_004"].str.contains("品川区")]
# print(shinagawa)

# m = gdf.explore(width=500, height=800)

# print(shinagawa.crs)
# print(gdf.crs)

# gdf.to_crs(epsg=6668, inplace=True)
# print(gdf.crs)

a = Point(0, 1)
b = Point(1, 1)
# print(a.distance(b))

tokyo_station = Point(139.767, 35.681)
tokyo_tower = Point(139.745, 35.659)
distance01 = tokyo_station.distance(tokyo_tower)
# print(distance01)

points_gdf = gpd.GeoDataFrame({"place": ["tokyo_station", "tokyo_tower"], "geometry": [tokyo_station, tokyo_tower]}, crs="EPSG:4326")
# print(points_gdf)

points_gdf = points_gdf.to_crs("EPSG:6691")
# print(points_gdf)

dist = points_gdf.loc[0, "geometry"].distance(points_gdf.loc[1, "geometry"])
# print(dist)

train_gdf.to_crs("EPSG: 6691", inplace=True)
# print(train_gdf)

# print(gyosei)
gyousei_temp = gyosei.dropna(subset=["N03_004"])
gyousei_ku = gyosei[gyosei["N03_004"].str.contains("区")]
gyousei_ku.to_crs("EPSG: 6691", inplace=True)

gyousei_area = gyousei_ku.geometry.area/10**6

pd.DataFrame(gyousei_ku).to_csv("output.csv", index=False)
# print(gyousei_ku)
# print(gyousei_area)

a = LineString([(0, 0), (5, 5)])
b = LineString([(2, 2), (10, 2)])
c = Point(2.5, 2.5)


m = train_gdf.explore()
shinagawa.explore(m=m, color="orange", marker_kwds={"radius": 3})
output_file = "train_exdata.html"
m.save(output_file)