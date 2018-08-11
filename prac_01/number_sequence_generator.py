'''
Program that calculates and list all the even, odd,  and square numbers
between two given whole numbers including negatives.
'''

import math

def main():
    x_value = int(input("Enter a value for x: "))
    y_value = int(input("Enter a value for y: "))
    print()
    print("Even numbers between", x_value, "and", y_value)
    for i in range (x_value, y_value + 1):                      # Lists even numbers in range
        if i % 2 == 0:
            print(i, end=' ')
    print()
    print()
    print("Odd numbers between", x_value, "and", y_value)       # Lists odd numbers in range
    for i in range (x_value, y_value + 1):
        if i % 2 == 1:
            print(i, end=' ')
    print()
    print()
    print("Square numbers between", x_value, "and", y_value)
    for i in range (x_value, y_value + 1):                      # Lists square numbers in range
        if i < 0:
            continue
        elif math.sqrt(i).is_integer():
            print(i, end=' ')

main()