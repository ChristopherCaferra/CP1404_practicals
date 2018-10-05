"""
CP1404/CP5632 Practical
SilverServiceTaxi class by Christopher Caferra
"""

from cp1404practicals.prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes fanciness and flagfall."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness=1.0):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        """Return a string like a Taxi but with flagfall"""
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """Get Taxi fare plus flagfall"""
        return super().get_fare() + self.flagfall
