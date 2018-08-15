"""
Inadequate security checker program
"""


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
            'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer','bob']
username_input = input("Enter your username: ")
while username_input not in usernames:
    print("Access denied")
print("Access granted")