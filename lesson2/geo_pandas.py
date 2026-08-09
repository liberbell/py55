import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString, Polygon

d = {"cal1": ["A", "B"], "geometry": [Point(0, 1), Point(1, 0)]}