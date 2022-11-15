import pandas as pd 
import plotly.express as px 

def plot_example():
    df = px.data.iris()
    fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", marginal_y="violin",
                       marginal_x="box", trendline="ols", template="simple_white")
    fig.show()

if __name__ == "__main__":
    plot_example()
