import pandas as pd

# Load the CSV file
df = pd.read_csv('input_documents/nsduh_data_codebook.csv')

# Extract unique values from the "Long_Description" column
unique_items = df['Long_Description'].unique()

# Convert the array of unique items to a list (if needed)
unique_items_list = unique_items.tolist()

# # Print the unique items
# for item in unique_items_list:
#     print(item)

# Specify the output text file path
output_file_path = 'unique_long_descriptions.txt'

# Write the unique items to the text file
with open(output_file_path, 'w') as file:
    for item in unique_items_list:
        file.write(f"{item}\n")

print(f"Unique items have been saved to {output_file_path}")
