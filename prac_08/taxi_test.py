from cp1404practicals.prac_08.taxi import Taxi

prius_one = Taxi("Prius1", 100)

print("Test initialisation:")
print(prius_one)

print("\nTest drive() method:")
prius_one.drive(40)
print(prius_one)

print("\nTest start_fare() method:")
prius_one.start_fare()
prius_one.drive(100)
print(prius_one, "\nFare:", prius_one.current_fare_distance)
