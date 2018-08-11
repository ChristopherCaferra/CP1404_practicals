"""
CP1404/CP5632 - Practical
program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    grade = calculate_grade(score)
    print("Final grade is: {}".format(grade))


def calculate_grade(score):
    # calculate grade and return string to main
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
