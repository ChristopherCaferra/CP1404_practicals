"""
CP1404/CP5632 Practical
Demos of various os module examples
"""

import os


def main():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))
        for name in filenames:
            old_name = os.path.join(directory_name, name)
            new_name = os.path.join(directory_name, get_fixed_filename(name))
            print(new_name)
            os.rename(old_name, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(".TXT", ".txt")
    new_text = ''
    for i, letter in enumerate(new_name):
        if letter.isupper() and not new_name[i - 1] == "(" and not new_name[i - 1] == " " \
                and not new_name[i - 1] == "_":
            new_text += ' '
        new_text += letter
    new_text = new_text[:new_text.find(".")].title().strip() + new_text[new_text.find("."):].strip()
    new_text = new_text.replace(" ", "_")
    return new_text


main()
