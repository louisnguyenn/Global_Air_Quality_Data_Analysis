import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import sys

def main():

    # reading the dataset as a dataframe using pandas using try-except block
    try: 
        df = pd.read_csv("air_quality_preprocessed_dataset.csv", encoding="utf-8-sig")
    
    except IOError as err:
        print("Unable to open pre-processed file 'air_quality_preprocessed_dataset.csv' : {}".format(err), file=sys.stderr)
        sys.exit(1)

    # using plotly to create a bar graph
    plotly_fig = px.bar(df, x="city", y="aqi", title="Air Quality Metrics in Cities")
    plotly_fig.show()

main()