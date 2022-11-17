import time
import webbrowser
import pandas as pd
import plotly.express as px
import requests
from keplergl import KeplerGl

def plot_example():
    """ Simple example of plotting using plotly
    """
    iris = px.data.iris()
    fig = px.scatter(iris, x="sepal_width", y="sepal_length", color="species", marginal_y="violin",
                       marginal_x="box", trendline="ols", template="simple_white")
    fig.show()

def api_example():
    """ Simple example of api requests
    """
    response = requests.get('https://api.github.com',timeout=10)
    resp_df = pd.json_normalize(response.json())
    print(resp_df)

def map_example():
    """ Simple map example using kepler
    """
    map_1 = KeplerGl()
    map_1.save_to_html(file_name='first_map.html')
    time.sleep(1)
    webbrowser.open('first_map.html', new=2)

if __name__ == "__main__":
    api_example()
    plot_example()
    map_example()
