"""Program to estimate Electricity bill costs over the biling period"""

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricty Bill Estimator")
print()
cents_per_kilowatts = int(input("Which tariff? 11 or 31: "))
while cents_per_kilowatts != 11 and cents_per_kilowatts != 31:
    print("Invalid selection.")
    cents_per_kilowatts = int(input("Which tariff? 11 or 31: "))
daily_electricity_usage = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))
print()
if cents_per_kilowatts == 11:
    estimated_bill = (TARIFF_11 * daily_electricity_usage) * billing_days
else:
    estimated_bill = (TARIFF_31 * daily_electricity_usage) * billing_days
print("Estimated bill: ${:,.2f}".format(estimated_bill))

