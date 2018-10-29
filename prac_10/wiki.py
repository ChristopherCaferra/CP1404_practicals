"""
CP1404/CP5632 Practical
Wiki
"""

import wikipedia

MENU = """(S)earch phrase
(P)age title"""


def main():
    """Search wikipedia pages and print the summary"""
    print(MENU)
    menu_input = input(">>> ").lower()
    while not menu_input == "":
        if menu_input == "s":
            search_input = input("What would you like to search?: ")
            try:
                search_result = wikipedia.search(search_input)
                print(wikipedia.summary(search_result))
            except wikipedia.exceptions.DisambiguationError as e:
                print(e.options)
        elif menu_input == "p":
            summary_input = input("What is the title of the page?: ")
            try:
                title_search = wikipedia.page(summary_input)
                print(wikipedia.page(title_search).title)
                print(wikipedia.summary(title_search))
                print(wikipedia.page(title_search).url)
            except wikipedia.exceptions.DisambiguationError as e:
                print(e.options)
        else:
            print("Invalid menu option. Type 'S' or 'P'.")
        print(MENU)
        menu_input = input(">>> ").lower()


main()
