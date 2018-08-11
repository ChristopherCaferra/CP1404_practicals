"""
CP1404/CP5632 - Practical
Program for calculating total cost of items sold at a shop
"""

total_price = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items")
    number_of_items = int(input("Number of items: "))

for i in range(number_of_items):
    item_price = float(input("Price of item: $"))
    total_price += item_price

if total_price > 100:
        total_price *= 0.9

print("Total price for {} items is ${:,.2f}".format(number_of_items, total_price))