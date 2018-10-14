"""
CP1404/CP5632 Practical
Program to sort files into directories based user input
By Christopher Caferra
"""

import  os
import shutil


def main():
    """Program to sort file extensions based on categories chosen by the user"""
    extensions = {}
    files = []
    os.chdir('FilesToSort')
    for filename in os.listdir('.'):        # save file names to list and extensions to dictionary
        file_type = filename[filename.find('.') + 1:]
        if filename.find(file_type):
            files.append(filename)
            extensions.update({file_type: ""})
    for extension in extensions.keys():     # get file category for every extension
        category = input("What category would you like to sort {} files into? ".format(extension))
        extensions.update({extension: category})
    for category in extensions.values():    # make file category folder if it does not exist already
        if not os.path.isdir(category):
            os.mkdir(category)
            print(category)
    for filename in files:                  # move files into category folders
        file_type = filename[filename.find('.') + 1:]
        shutil.move(filename, extensions.get(file_type) + "/" + filename)


main()
