def liters_100km_to_miles_gallon(liters):
    meters_per_mile = 1609.344
    liters_per_gallon = 3.785411784

def miles_gallon_to_liters_100km(miles):
    meters_per_mile = 1609.344
    liters_per_gallon = 3.785411784

print(liters_100km_to_miles_gallon(3.9))  # 60.31143162393162
print(liters_100km_to_miles_gallon(7.5))  # 31.36194444444444
print(liters_100km_to_miles_gallon(10.))  # 23.52145833333333
print(miles_gallon_to_liters_100km(60.3)) # 3.9007393587617467
print(miles_gallon_to_liters_100km(31.4)) # 7.490910297239916
print(miles_gallon_to_liters_100km(23.5)) # 10.009131205673757
