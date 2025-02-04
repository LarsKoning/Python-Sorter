import os
import shutil
from os import listdir
from os.path import isfile, join

# The path to the downloads folder or the folder you want to sort
file_path = os.path.expanduser('~/Downloads')  # Uses home directory dynamically

# Define file types and their relative destination folders
filetype_dict = {
    'pdf': 'Documents',
    'docx': 'Documents',
    'txt': 'Text_Files',
    'jpg': 'Images',
    'png': 'Images',
    'mp4': 'Videos',
    'mov': 'Videos',
    'mp3': 'Music',
    'wav': 'Music',
    'zip': 'Archives',
    'tar': 'Archives',
    'pptx': 'Powerpoints',
}

# Default folder for unknown file types
default_folder = os.path.join(file_path, "Other")

# Obtain all files in the designated folder
files = [f for f in listdir(file_path) if isfile(join(file_path, f))]

# Create necessary folders if they don't exist
for folder in filetype_dict.values():
    folder_path = os.path.join(file_path, folder)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

# Create the "Other" folder if it doesn't exist
if not os.path.exists(default_folder):
    os.mkdir(default_folder)

# Dry Run Mode (Simulation)
simulate = True  # Set to False to actually move files

# Move files to designated folders or "Other"
for i, file in enumerate(files, start=1):
    if '.' in file:
        filetype = file.split('.')[-1].lower()  # Extract file extension
    else:
        filetype = "unknown"  # Treat files without extensions as "unknown"

    # Determine destination folder
    if filetype in filetype_dict:
        dest_folder = os.path.join(file_path, filetype_dict[filetype])
    else:
        dest_folder = default_folder  # Move unknown files to "Other"

    src_path = os.path.join(file_path, file)
    dest_path = os.path.join(dest_folder, file)

    if simulate:
        print(f"Simulated: {src_path} >>> {dest_path}")  # Dry run log
    else:
        shutil.move(src_path, dest_path)  # Move the file if simulate = false
        print(f"{i}. {file} >>> Moved to {dest_folder}")
