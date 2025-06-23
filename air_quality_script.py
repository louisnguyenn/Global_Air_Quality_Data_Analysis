import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import sys

def get_aqi_color(aqi_value):
    if aqi_value <= 50:
        return '#00E400'      # green

    elif aqi_value <= 100:
        return '#FFFF00'      # yellow

    elif aqi_value <= 150:
        return '#FF7E00'      # orange

    elif aqi_value <= 200:
        return '#FF0000'      # red

    elif aqi_value <= 300:
        return '#8F3F97'      # purple

    else:
        return '#7E0023'      # maroon

def main():

    # reading the dataset as a dataframe using pandas using try-except block
    try: 
        df = pd.read_csv("air_quality_preprocessed_dataset.csv", encoding="utf-8-sig")
    
    except IOError as err:
        print("Unable to open pre-processed file 'air_quality_preprocessed_dataset.csv' : {}".format(err), file=sys.stderr)
        sys.exit(1)

    df['color'] = df['aqi'].apply(get_aqi_color)
    
    # Create bar chart with custom colors
    fig = px.bar(df, 
                 x="city", 
                 y="aqi", 
                 title="Air Quality Metrics in Cities",
                 color='color',
                 color_discrete_map='identity')  # Use the actual color values

    # using plotly to create a bar graph
    # fig = px.bar(df, x="city", y="aqi", title="Air Quality Metrics in Cities")
    fig.show()

main()
