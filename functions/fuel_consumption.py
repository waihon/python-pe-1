def liters_100km_to_miles_gallon(liters):
    meters_per_mile = 1_609.344
    km_per_mile = meters_per_mile / 1_000
    liters_per_gallon = 3.785411784

    liters_per_km = liters / 100 # km
    km_per_liter = 1 / liters_per_km
    miles_per_liter = km_per_liter / km_per_mile
    miles_per_gallon = miles_per_liter * liters_per_gallon

    return miles_per_gallon

def miles_gallon_to_liters_100km(miles):
    meters_per_mile = 1609.344
    km_per_mile = meters_per_mile / 1_000
    liters_per_gallon = 3.785411784

    gallon_per_mile = 1 / miles # per gallon
    liters_per_mile = gallon_per_mile * liters_per_gallon
    liters_per_km = liters_per_mile / km_per_mile
    liters_per_100km = liters_per_km * 100

    return liters_per_100km

print(liters_100km_to_miles_gallon(3.9))  # 60.31143162393162
print(liters_100km_to_miles_gallon(7.5))  # 31.36194444444444
print(liters_100km_to_miles_gallon(10.))  # 23.52145833333333
print(miles_gallon_to_liters_100km(60.3)) # 3.900739358761747
print(miles_gallon_to_liters_100km(31.4)) # 7.490910297239915
print(miles_gallon_to_liters_100km(23.5)) # 10.009131205673757
