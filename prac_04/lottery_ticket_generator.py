"""
CP1404/CP5632 Practical Lottery
quick pick generator program
"""

import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    """Lottery quick pick program. Picks random numbers for lottery"""
    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks < 0:
        print("Invalid number")
        number_of_quick_picks = int(input("How many quick picks? "))

    for i in range(number_of_quick_picks):  # loops to add random numbers to quick picks
        quick_pick = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()

        print(" ".join("{:2}".format(number) for number in quick_pick))


main()