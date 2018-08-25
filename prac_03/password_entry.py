"""Program that checks user input password for correct length"""

MINIMUM_PASSWORD_LENGTH = 6


def main():

    password = get_password()

    print_asterisks(password)


def print_asterisks(string):
    # Prints "*" for every character in string.
    asterisks = len(string) * "*"
    print(asterisks)


def get_password():
    password = input("Enter password: ")
    while len(password) < MINIMUM_PASSWORD_LENGTH:  # Check password against length requirements.
        print("Password is too small. Must be {} characters long.".format(MINIMUM_PASSWORD_LENGTH))
        password = input("Enter password: ")
    return password


main()
