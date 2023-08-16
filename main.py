filepath= "filename.txt"
arrfile = []

with open(filepath, "r", encoding="utf-8") as file:
    for line in file:
        arrfile.append(line.strip())

import os
import shutil

# Directory paths
source_directory = 'C:/file/pdf'
destination_directory = 'C:/file/dest'

# Function to copy files
def copy_files(file_list, source_dir, dest_dir):
    for file_name in file_list:
        source_file_path = os.path.join(source_dir, file_name)
        dest_file_path = os.path.join(dest_dir, file_name)
        if os.path.exists(source_file_path):
            try:
                shutil.copyfile(source_file_path, dest_file_path)
                print(f"File '{file_name}' copied successfully.")
            except Exception as e:
                print(f"Error copying '{file_name}': {e}")
        else:
            print(f"File '{file_name}' does not exist in the source directory.")

# Call the function
copy_files(arrfile, source_directory, destination_directory)