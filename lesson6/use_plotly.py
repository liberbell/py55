import plotly.express as px

df = px.data.gapminder()
# print(df)

# figure = px.scatter(df, x="gdpPercap", y="lifeExp", log_x=True, hover_name="continent")

figure = px.choropleth(df[df["year"]==2007], locations="iso_alpha", color="gdpPercap")

# figure.show()