"""
CP1404/CP5632 Practical
Program to sort files into directories based user input
"""

import  os
import shutil


def main():
    extensions = {}
    files = []
    os.chdir('FilesToSort')

    for filename in os.listdir('.'):
        file_type = filename[filename.find('.') + 1:]
        if filename.find(file_type):
            files.append(filename)
            extensions.update({file_type: ""})

    for extension in extensions.keys():
        category = input("What category would you like to sort {} files into? ".format(extension))
        extensions.update({extension: category})

    for category in extensions.values():
        if not os.path.isdir(category):
            os.mkdir(category)
            print(category)

    for filename in files:
        file_type = filename[filename.find('.') + 1:]
        shutil.move(filename, extensions.get(file_type) + "/" + filename)



main()
