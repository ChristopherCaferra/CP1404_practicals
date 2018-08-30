"""
CP1404 prac_06.languages by Christopher Caferra
Program that outputs basic method use from class ProgrammingLanguage.
"""

from cp1404practicals.prac_06.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

programming_languages = [ruby, python, visual_basic]


def main():
    print(ruby)
    print(python)
    print(visual_basic)

    print("The dynamically typed languages are:")
    for language in programming_languages:
        if language.is_dynamic():
            print(language.name)


main()
