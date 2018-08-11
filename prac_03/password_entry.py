"""Check user input password for correct length"""


def main():

    minimum_password_length = 6
    password = input("Enter password: ")

    while len(password) < minimum_password_length:  # Check password against length requirements.
        print("Password is too small. Must be {} characters long.".format(minimum_password_length))
        password = input("Enter password: ")

    for char in password:   # Print "*" for every character in password.
        print("*", end='')


main()