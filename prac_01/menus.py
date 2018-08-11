"""
Basic menu program that exits when quit is selected
"""

menu = """(H)ello
(G)oodbye
(Q)uit"""

def main():
    user_name = input("Enter name: ")
    print(menu)
    print()
    menu_choice = str(input(">>> "))
    while menu_choice != "Q" and menu_choice != "q":
        if menu_choice == "H" or menu_choice == "h":
            print("Hello", user_name)
        elif menu_choice == "G" or menu_choice == "g":
            print("Goodbye", user_name)
        else:
            print("Invalid choice")
        print(menu)
        print()
        menu_choice = str(input(">>> "))
    print("Finished")

main()