"""Program to show code that reads and writes to and from files."""


out_file = open('name.txt', 'w')
user_name = input("Enter your name: ")
print(user_name, file=out_file)     # Writes output to .txt file
out_file.close()


in_file = open('name.txt', 'r')
user_name = in_file.read().strip()
print('Your name is', user_name)    # Prints output from .txt file
in_file.close()


in_file = open('numbers.txt', 'r')  # Sum of 2 numbers from single .txt file
first_number = int(in_file.readline())
second_number = int(in_file.readline())
result = first_number + second_number
print(result)
in_file.close()


in_file = open('numbers.txt', 'r')
total = 0
for line in in_file:                # Sum of all numbers from single .txt file
    number_in_line = int(line)
    total += number_in_line
print(total)
in_file.close()