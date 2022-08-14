#!/usr/bin/env python 3
# move_video_files.py - copies videos to another location
'''When exporting Google Photos via Takeout it is not possible
to separate videos. Keep videos in a different location on your
computer or move only photos to a service like Amazon Photos that
doesn't allow large amounts of video files.'''

# When running, select folder desired from pop-up window

import os
import shutil
from pathlib import Path
from tkinter.filedialog import askdirectory

# select Google Photos or parent photo/video folder
folder = askdirectory()
folder_path = Path(folder)
os.chdir(folder_path)

# create destination folder for videos
destination = Path('../' + str(folder_path.stem) + '_videos')
os.makedirs(destination, exist_ok=True)

# Walk the entire folder tree.
for folder_name, subfolders, filenames in os.walk(folder):
    print(f'Checking files in {folder_name}...')
    for filename in filenames:
        f = filename.lower()
        # add any other extensions desired
        for ext in ['.mp4', '.mov', '.wmv', '.avi', '.flv']:
            if f.endswith(ext):
                print(f'Moving {filename}...')
                file = Path(filename)
                p = Path(destination) / filename
                number = 0
                new_name = None
                # renames different files with the same name
                while p.exists():
                    number += 1
                    new_name = file.stem + str(number) + file.suffix
                    # check if filename + number already exists
                    p = Path(destination) / new_name
                # move the files to destination folder
                if new_name: 
                    shutil.move(
                        Path(folder_name) / filename, destination / new_name
                    )
                else:
                    shutil.move(Path(folder_name) / filename, destination)
            
print('Done.')
