"""CP1401 prac_04. Program to add numbers to a list """


def main():
    numbers = []
    for i in range(5):
        validated = False
        while not validated:
            try:
                number = int(input("Number: "))
                numbers.append(number)
                validated = True
            except ValueError:
                print("invalid input")
    average_of_numbers_list = calculate_average_of_list_numbers(numbers)
    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The average of the numbers is {}".format(average_of_numbers_list))


def calculate_average_of_list_numbers(list):
    sum_of_list = sum(list)
    average_of_list = sum_of_list / len(list)
    return average_of_list


main()