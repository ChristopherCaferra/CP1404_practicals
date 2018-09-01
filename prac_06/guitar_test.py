"""
CP1404 prac_06.guitar_test by Christopher Caferra
Test program to view functionality of new class 'Guitar'
"""

from cp1404practicals.prac_06.guitar import Guitar


def main():

    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    blackjack = Guitar("Blackjack SLS C-1 FR-S", 2012, 1199.95)

    print(gibson)
    print(blackjack, "\n")
    print("{} get_age() - Expected 96. Got {}".format(gibson.name, gibson.get_age()))
    print("{} is_vintage() - Expected True. Got {}\n".format(gibson.name, gibson.is_vintage()))
    print("{} get_age() - Expected 6. Got {}".format(blackjack.name, blackjack.get_age()))
    print("{} is_vintage() - Expected False. Got {}".format(blackjack.name, blackjack.is_vintage()))

main()
