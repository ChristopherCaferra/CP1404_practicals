"""
CP1404 prac_06.date by Christopher Caferra - Extension Work
Class for Date input
"""


class Date:
    """ Represents a Date. """

    months_list = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    def __init__(self, days=0, month=0, year=0):
        """ Initialise Date instance. """
        self.days = days
        self.month = month
        self.year = year

    def __str__(self):
        """ String method for Date. """
        return "{}/{}/{}".format(self.days, self.month, self.year)

    def add_days(self, number):
        """ Add number of days to Date. """
        self.days += number
        while self.days > self.months_list[self.month - 1]:
            if self.is_leap_year() and self.month == 2:
                self.days -= 29
            else:
                self.days -= self.months_list[self.month - 1]
            self.month += 1
            if self.month == 13:
                self.month = 1
                self.year += 1

    def is_leap_year(self):
        """ Define if date is a leap year. """
        if (self.year / 4).is_integer():
            return True
        return False



