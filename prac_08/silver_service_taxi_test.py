"""Test code for SilverServiceTaxi class"""

from cp1404practicals.prac_08.silver_service_taxi import SilverServiceTaxi

print("test initialisation:")
hummer = SilverServiceTaxi("Hummer", 200, 4)
print(hummer)
silver_taxi = SilverServiceTaxi("Limo", 200, 2)
print(silver_taxi)
print("\ntest start_fare() and drive():")
silver_taxi.start_fare()
silver_taxi.drive(18)
print(silver_taxi)
print("\ntest get_fare()")
print("fare is ${:.2f}".format(silver_taxi.get_fare()))

