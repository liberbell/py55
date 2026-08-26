import pandas as pd
import geopandas as gpd
import plotly.express as px
import numpy as np

# df = pd.read_csv("data/owid-covid-latest.csv", encoding="utf-8")
df = pd.read_csv("data/owid-covid-data-last-ecdc.csv", encoding="utf-8")
print(df)