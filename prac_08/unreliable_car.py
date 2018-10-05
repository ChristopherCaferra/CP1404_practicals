"""
CP1404/CP5632 Practical
UnreliableCar class by Christopher Caferra
"""

from cp1404practicals.prac_08.car import Car
import random


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return a string like a Car but with reliability."""
        return "{}, reliability = {}".format(super().__str__(), self.reliability)

    def drive(self, distance):
        """Drive like parent Car but only if car is reliable."""
        if random.randint(0, 101) < self.reliability:
            super().drive(distance)
        return distance
