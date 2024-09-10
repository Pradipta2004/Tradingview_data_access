import pandas as pd

# Replace 'your_file.csv' with the path to your .csv file
file_path = 'output_file.csv'

# Read the .csv file into a DataFrame
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
print(df.head())
