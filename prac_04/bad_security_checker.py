"""
Inadequate security checker program
"""


def main():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    username_input = input("Enter your username: ")
    print(check_username(username_input, usernames))


def check_username(string, usernames):
    while string not in usernames:
        print("Access denied")
        string = input("Enter your username: ")
    return "Access granted"


main()
