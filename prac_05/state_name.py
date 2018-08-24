""" CP1404/CP5632 Practical State names in a dictionary. """

STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}


def main():
    for abbreviation, state in STATE_NAMES.items():
        print("{:3} is {}".format(abbreviation, state))
    print("")
    state = input("Enter short state: ").upper()
    while state != "":
        if state in STATE_NAMES:
            print(state, "is", STATE_NAMES[state])
        else:
            print("Invalid short state")
        state = input("Enter short state: ").upper()


main()
