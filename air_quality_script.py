import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys

def main():
    # reading the dataset as a dataframe using pandas using try-except block
    try: 
        df = pd.read_csv("air_quality_preprocessed_dataset.csv", encoding="utf-8-sig")
    
    except IOError as err:
        print("Unable to open pre-processed file 'air_quality_preprocessed_dataset.csv' : {}".format(err), file=sys.stderr)
        sys.exit(1)
    
    # create the matplotlib plot (bar graph)
    # plt.figure()
    
    # bars = plt.bar(df['city'], df['aqi'])

    # # customize the plot
    # plt.title("Air Quality Metrics in Cities")
    # plt.xlabel("City")
    # plt.ylabel("Air Quality Index (AQI)")
    
    # # rotate city names for better readability
    # plt.xticks(rotation=45, ha='right', fontsize=10)
    # plt.yticks(fontsize=10)
        
    # plt.show()

    # histogram plot
    # df.plot.hist()
    # plt.show()

    plt.figure()

    city_avg = df.groupby('city')['aqi'].mean().sort_values(ascending=False)

    bars = plt.bar(city_avg.index, city_avg.values)

    plt.title("Average Air Quality Index by City")
    plt.xlabel("City")
    plt.ylabel("Average AQI")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    plt.show()

main()
