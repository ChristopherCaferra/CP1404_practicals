"""
Program that calculates a change in the population each year over a 10 year period
"""

import random

INCREASE_PERCENTAGE = random.randrange(10,21)
DECREASE_PERCENTAGE = random.randrange(5,26)
NUMBER_OF_YEARS = 10


def main():
    population = 1000
    print("Welcome to the gopher population simulator!")
    print("Starting population: {}".format(population))
    for year in range(1, NUMBER_OF_YEARS + 1):                   # Loop to print predicted data over a 10 year period.
        population_increase = calculate_population_increase(population)
        population_decrease = calculate_population_decrease(population)
        population = calculate_new_population(population, population_increase, population_decrease)
        print("\nyear {} \n{} were born. {} died. "
              "\nPopulation: {}".format(year, population_increase, population_decrease, population))


def calculate_population_increase(population):
    increase = population * (INCREASE_PERCENTAGE / 100)
    increase = int(increase)
    return increase


def calculate_population_decrease(population):
    decrease = population * (DECREASE_PERCENTAGE / 100)
    decrease = int(decrease)
    return decrease


def calculate_new_population(population, increase, decrease):
    population += increase - decrease
    return population


main()
