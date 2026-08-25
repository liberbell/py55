import plotly.express as px

df = px.data.gapminder()
# print(df)

figure = px.scatter(df, x="gdpPercap", y="lifeExp", log_x=True)
figure.show()