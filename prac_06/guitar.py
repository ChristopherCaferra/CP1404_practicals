"""
CP1404 prac_06.guitar by Christopher Caferra
Class for storing information about guitars.
"""


class Guitar:
    """ Represent a guitar object. """

    def __init__(self, name, year=0, cost=0):
        """ Initialise a guitar instance. """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """ String format for class. """
        return "{} ({}) : ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        """ Get age of the guitar. """
        age = 2018 - self.year
        return age

    def is_vintage(self):
        """ Check if the guitar is over 50 years old. """
        if self.get_age() >= 50:
            return True
        else:
            return False
