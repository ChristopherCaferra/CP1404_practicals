"""
CP1404/CP5632 Practical
Taxi Simulator
"""

from cp1404practicals.prac_08.silver_service_taxi import Taxi, SilverServiceTaxi

menu = "q)uit, c)hoose taxi, d)rive"


def main():
    """Simulate the cost of catching different taxis based on distance traveled"""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    km_traveled = 0
    total_bill = 0.00
    print("Lets drive!")
    print(menu)
    menu_selection = input(">>>").lower()
    while menu_selection != "q":
        if menu_selection == "c":
            current_taxi = choose_taxi(taxis)
        if menu_selection == "d":
            if current_taxi is None:
                print("Please select a taxi first")
            else:
                total_bill, km_traveled = drive_taxi(current_taxi, total_bill, km_traveled)
        print("Bill to date: ${:.2f}".format(total_bill))
        print("Kilometers traveled: {}".format(km_traveled))
        print(menu)
        menu_selection = input(">>>").lower()
    print("Total trip cost: ${:.2f}".format(total_bill))
    if current_taxi is None:
        print("You did not choose any taxis.")
    else:
        print("Taxis are now:")
        print_taxis(taxis)


def choose_taxi(taxis):
    """Choose taxi to catch from printed list of taxis"""
    print("Taxis available:")
    print_taxis(taxis)
    taxi_number = get_valid_taxi_number(taxis)
    current_taxi = taxis[taxi_number]
    return current_taxi


def print_taxis(taxis):
    """Print a list of taxis"""
    car_count = 0
    for car in taxis:
        try:
            print("{} - {}, fanciness: {}, fare: ${:.2f} plus flagfall: ${:.2f}".format(car_count, car.name,
                                                                                        car.fanciness, car.price_per_km,
                                                                                        car.flagfall))
        except AttributeError:
            print("{} - {}, fare: ${:.2f}".format(car_count, car.name, car.price_per_km,))
        car_count += 1


def get_valid_taxi_number(taxis):
    """Get valid integer for taxi in list"""
    taxi_number = 0
    validated = False
    while not validated:
        try:
            taxi_number = int(input("Choose taxi: "))
            while taxi_number < 0 or taxi_number > len(taxis) - 1:
                taxi_number = int(input("invalid taxi number\nChoose taxi: "))
            validated = True
        except ValueError:
            print("Invalid input. Enter a number between 0 - {}".format(len(taxis) - 1))
    return taxi_number


def get_valid_distance():
    """Get valid integer for distance"""
    distance = 0
    validated = False
    while not validated:
        try:
            distance = int(input("Drive how far?: "))
            while distance < 0 :
                distance = int(input("invalid distance. Must be 0 or greater\nDrive how far?: "))
            validated = True
        except ValueError:
            print("Invalid input. Enter a number.")
    return distance


def drive_taxi(current_taxi, total_bill, km_traveled):
    """drive taxi and calculate fare"""
    start_odometer = current_taxi.odometer
    distance = get_valid_distance()
    current_taxi.start_fare()
    current_taxi.drive(distance)
    total_bill += current_taxi.get_fare()
    km_traveled += (current_taxi.odometer - start_odometer)
    print("Your {} trip cost ${:.2f}".format(current_taxi.name, current_taxi.get_fare()))
    return total_bill, km_traveled


main()
