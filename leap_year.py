year = int(input("Enter a year: "))
leap_year = None

if year < 1582:
    print("Not within the Gregorian calendar period")
    exit()

if year % 4 != 0:
    leap_year = False
elif year % 100 != 0:
    leap_year = True
elif year % 400 != 0:
    leap_year = False
else:
    leap_year = True

if leap_year:
    print("Leap year")
else:
    print("Common year")

"""
Test Data
Sample input: 2000
Expected output: Leap year

Sample input: 2015
Expected output: Common year

Sample input: 1999
Expected output: Common year

Sample input: 1996
Expected output: Leap year

Sample input: 1900
Expected output: Common Year

Sample input: 1580
Expected output: Not within the Gregorian calendar period
"""
