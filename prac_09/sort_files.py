"""
CP1404/CP5632 Practical
Program to sort files into directories based on file type
"""

import os
import shutil


def main():
    os.chdir('FilesToSort')
    for filename in os.listdir('.'):
        file_type = filename[filename.find('.') + 1:]
        if os.path.isdir(filename):
            continue
        else:
            try:
                os.mkdir(file_type)
            except FileExistsError:
                pass
        shutil.move(filename, file_type + '/' + filename)


main()
