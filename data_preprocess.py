import pandas as pd
import sys
import csv

def main():

    # open the dataset using try-except block
    try:
        input_dataset = open("air_quality_health_dataset.csv", "r", newline='', encoding="utf-8-sig")

    except IOError as err:
        print("Unable to open input file 'air_quality_health_dataset.csv' : {}".format(err), file=sys.stderr)
        sys.exit(1)

    # open an output file to use for data analysis in write mode
    try:
        output_dataset = open("air_quality_preprocessed_dataset.csv", "w", newline='', encoding="utf-8-sig")

    except IOError as err:
        print("Unable to open output file 'air_quality_preprocessed_dataset.csv' : {}".format(err), file=sys.stderr)
        sys.exit(1)

    # reading the dataset using a csv reader
    file_reader = csv.reader(input_dataset)

    # skipping the first row (header) of the csv file
    next(file_reader, None)

    # creating a variable to write onto the output file
    dataset_writer = csv.writer(output_dataset)

    dataset_writer.writerow(["city", "aqi"])

    print("Pre-processing dataset...")
    # pre process the required data from the csv
    for row in file_reader:
        city = row[0]
        aqi = row[2]

        # filtering the dataset with the requried cities
        if city == "Delhi" or city == "Beijing" or city == "Mexico City" or city == "Los Angeles" or city == "London" or city == "Tokyo" or city == "Cairo" or city == "São Paulo":
            dataset_writer.writerow([city, aqi])

    print("Pre-processing finished.")
main()
