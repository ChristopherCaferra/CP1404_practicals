"""Check user input password for correct length"""

MINIMUM_PASSWORD_LENGTH = 6


def main():

    password = get_password()

    print_asterisks(password)


def print_asterisks(password):
    for char in password:  # Print "*" for every character in password.
        print("*", end='')


def get_password():
    password = input("Enter password: ")
    while len(password) < MINIMUM_PASSWORD_LENGTH:  # Check password against length requirements.
        print("Password is too small. Must be {} characters long.".format(MINIMUM_PASSWORD_LENGTH))
        password = input("Enter password: ")
    return password


main()