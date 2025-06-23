import pandas as pd

# passing the dataset as an commandline argument
dataset = argv[1]

# reading the dataset using pandas csv reader
df = pd.read_csv(dataset)
display(df)
