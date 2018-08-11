MINIMUM_NUMBER = 33
MAXIMUM_NUMBER = 127

# character_input = input("Enter a character: ")
# character_code = ord(character_input)
# print("The ASCII code for {} is {}".format(character_input, character_code))
#
# number_input = int(input("Enter a number between {} and {}: ".format(MINIMUM_NUMBER, MAXIMUM_NUMBER)))
# while number_input < MINIMUM_NUMBER or number_input > MAXIMUM_NUMBER:
#     print("Number is not in valid range.")
#     number_input = int(input("Enter a number between {} and {}: ".format(MINIMUM_NUMBER, MAXIMUM_NUMBER)))
# number_code = chr(number_input)
# print("The character for {} is {}".format(number_input, number_code))

for numbers in range(MINIMUM_NUMBER, MAXIMUM_NUMBER + 1, 1):
    print(numbers, chr(numbers))