import pandas as pd

def main():

    # open an output file to use for data analysis in write mode
    try:
        output_dataset = open("air_quality_preprocessed_dataset", "w", newline='', encoding="utf-8-sig")

    except IOError as err:
        print("Unable to open output file 'air_quality_preprocessed_dataset' : {}".format(err), file=sys.stderr)
        sys.exit(1)

    # reading the dataset using a csv reader
    data = pd.read_csv("air_quality_health_dataset.csv")

    # skipping the header of the csv file
    next(dataset_reader, None)

    # creating a variable to write onto the output file
    dataset_writer = csv.writer(air_quality_preprocessed_dataset)

    # pre process the required data from the csv
    for row in data:
        city = row[0]
        air_quality = row[2]

        if city == "Delhi":
            
