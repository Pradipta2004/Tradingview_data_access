import pandas as pd
# Replace 'input_file.csv' with the path to your .csv file
input_file = 'nifty.csv'

# Read the .csv file into a DataFrame
dff = pd.read_csv(input_file)

# Drop the second column (index 1)
dff = dff.drop(dff.columns[1], axis=1)

# Save the DataFrame back to a new .csv file
# Replace 'output_file.csv' with the desired output file path
output_file = 'output_file.csv'
dff.to_csv(output_file, index=False)
