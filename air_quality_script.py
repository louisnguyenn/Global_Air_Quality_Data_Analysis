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
    
    # create the matplotlib plot
    plt.figure()
    
    bars = plt.bar(df['city'], df['aqi'],  
                edgecolor='black', 
                linewidth=0.8,
                alpha=0.9)

    # customize the plot
    plt.title("Air Quality Metrics in Cities", 
              fontsize=20, 
              fontweight='bold', 
              pad=20)
    plt.xlabel("City", fontsize=14, fontweight='bold')
    plt.ylabel("Air Quality Index (AQI)", fontsize=14, fontweight='bold')
    
    # rotate city names for better readability
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.yticks(fontsize=10)
    
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    
    plt.tight_layout()
    
    plt.show()

main()
