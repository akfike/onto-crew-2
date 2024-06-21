import pandas as pd

# Load the data from the CSV file
df = pd.read_csv('input_documents/nsduh_data_codebook.csv')

# List of provided Question_Code values
question_code_list = [
    'BKMVTHFT', 
    'BKLARCNY', 
    'BKBURGL', 
    'BKSRVIOL', 
    'BKSMASLT', 
    'BKROB', 
    'BKARSON', 
    'BKDRVINF', 
    'DRVINALCO',
    'DRVINMARJ',
    'DRVINCOCN',
    'DRVINHERN',
    'DRVINHALL',
    'DRVININHL',
    'DRVINMETH',
    'DRVINALON',
    'BKDRUNK',
    'BKPOSTOB',
    'BKPOSTOB',
    'BKDRUG',
    'BKSEXNR',
    'BKFRAUD',
    'BKOTH',
    'BKOTHOF2'    
] 

# Filter the DataFrame based on the Question_Code values
filtered_df = df[df['Question_Code'].isin(question_code_list)]

# Extract the Long_Description values and ensure they are strings
long_descriptions = filtered_df['Long_Description'].astype(str).unique().tolist()

# Save each unique Long_Description value to a text file
with open('long_descriptions.txt', 'w') as file:
    for description in long_descriptions:
        file.write(description + '\n')
