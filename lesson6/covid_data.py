import pandas as pd
import geopandas as gpd
import plotly.express as px
import numpy as np

# df = pd.read_csv("data/owid-covid-latest.csv", encoding="utf-8")
df = pd.read_csv("data/owid-covid-data-last-ecdc.csv", encoding="utf-8")
# print(df)

# print(df[df["location"] == "Japan"])
# print(df.dtypes)

df_test = df[df["date"] == "2020-11-20"]
print(df_test)

avg_cases = df_test["new_cases"].median()
# px.choropleth(df_test, locations="iso_code", color="new_cases", range_color=[0, 10000], color_continuous_midpoint=avg_cases).show()

df_test["log_cases"] = df["new_cases"].apply(np.log10)
# px.choropleth(df_test, locations="iso_code", color="log_cases", range_color=[0, 6], color_continuous_midpoint=avg_cases).show()

df["date_yyyymm"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m")

df_month_mean = df.groupby(["date_yyyymm", "iso_code", "location"]).mean(numeric_only=True).reset_index()
px.choropleth(df_month_mean, locations="iso_code", color="new_cases", range_color=[0, 6], animation_frame="date_yyyymm").show()

# print(df_month_mean)