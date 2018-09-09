"""
CP1404 prac_06.guitars by Christopher Caferra
Program that creates a list of guitars and displays them in a formatted list.
"""

from cp1404practicals.prac_06.guitar import Guitar


def main():
    """ Main program. Get input from user and add it to list until user input is blank and print list. """
    guitars = []
    print("My guitars!")
    guitar_name = input("Name: ")
    while guitar_name != "":
        year, cost = get_guitar_info()
        guitars = add_guitar_to_list(guitars, guitar_name, year, cost)
        guitar_name = input("Name: ")
    print_list_of_guitars(guitars)


def print_list_of_guitars(guitars):
    """ Print a list of guitars with formatting and display if the guitar is vintage. """
    for i, guitar in enumerate(guitars):
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = "(Vintage)"
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                                   vintage_string))


def add_guitar_to_list(list, name, year, cost):
    """ Take in a list of guitars and append a new guitar to the list. """
    list.append(Guitar(name, year, cost))
    print("{} ({}) : ${} added.".format(name, year, cost))
    return list


def get_guitar_info():
    """ Get the year the guitar was made, and the cost fom user. """
    year = int(input("Year: "))
    cost = int(input("Cost: "))
    return year, cost


main()
