from cp1404practicals.prac_08.unreliable_car import UnreliableCar

car_one = UnreliableCar("Commodore", 100, 20)

print("Test initialisation:")
print(car_one)

print("\nTest drive() method:")
while car_one.odometer == 0:
    car_one.drive(20)
    if car_one.odometer == 0:
        print("Drive failed")
print("Drive successful")
print(car_one)



