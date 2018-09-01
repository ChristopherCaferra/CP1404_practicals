"""
CP1404 prac_06.programming_language by Christopher Caferra
Class containing details  of different programming languages.
"""


class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year=0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing is "Dynamic":
            return True
        else:
            return False

    def __str__(self):
        return "{}, {}, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection, self.year)
