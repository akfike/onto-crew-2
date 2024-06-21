import os

# Specify the folder containing the markdown files
folder_path = 'output_documents/OntoGeneration/gpt-4'  # Replace with your folder path

# List to store the paths of markdown files
markdown_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.md')]

# Path to the output merged file
output_file = 'incident_types.md'

# Open the output file in write mode
with open(output_file, 'w') as outfile:
    for filename in markdown_files:
        if os.path.isfile(filename):  # Check if the file exists
            with open(filename, 'r') as infile:
                outfile.write(infile.read())
                outfile.write('\n\n')  # Add some spacing between files (optional)
        else:
            print(f"File {filename} not found!")

print(f"All files have been merged into {output_file}")
