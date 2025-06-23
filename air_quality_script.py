import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def main()
    plotly_fig = px.bar(df, x="city", y="aqi", title="Air Quality Metrics in Cities")
    plotly_fig.show()

    print("Column names:")
    print(df.columns.tolist())