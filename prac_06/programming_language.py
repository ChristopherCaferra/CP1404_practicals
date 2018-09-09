"""
CP1404 prac_06.programming_language by Christopher Caferra
Class containing details  of different programming languages.
"""


class ProgrammingLanguage:
    """ Represents  programming language object. """

    def __init__(self, name, typing, reflection, year=0):
        """ Initialise a programming language. """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """ Check if programming language is dynamic. """
        if self.typing is "Dynamic":
            return True
        else:
            return False

    def __str__(self):
        """ String format for class. """
        return "{}, {}, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection, self.year)
