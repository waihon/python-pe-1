income = float(input("Enter the annual income: "))

if income <= 85_528:
    tax = (income * 0.18) - 556 # tax relief
else:
    tax = 14_839 + (income - 85_528) * 0.32

tax = max(round(tax, 0), 0)
print("The tax is:", tax, "thalers")

"""
Test Data
Sample input: 10000
Expected output: The tax is: 1244.0 thalers

Sample input: 100000
Expected output: The tax is: 19470.0 thalers

Sample input: 1000
Expected output: The tax is: 0.0 thalers

Sample input: -100
Expected output: The tax is: 0.0 thalers
"""
