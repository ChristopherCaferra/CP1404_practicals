"""
CP1404/CP5632 - Practical
3 different For loops testing range
"""

for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

number_of_stars = int(input("Enter number of stars: "))
for i in range(number_of_stars):
    print("*", end=' ')
print()

for i in range(number_of_stars):
    print("*"*(i+1))