def liters_100km_to_miles_gallon(liters):
    gallon_100km = liters / 3.785411784
    gallon_100miles = gallon_100km * 1.609344
    gallon_mile = gallon_100miles / 100
    miles_gallon = 1 / gallon_mile
    
    return miles_gallon

def miles_gallon_to_liters_100km(miles):
    miles_liter = miles / 3.785411784
    km_liter = miles_liter * 1.609344
    l00km_liter = km_liter / 100
    liters_100km = 1 / l00km_liter
    
    return liters_100km

print(liters_100km_to_miles_gallon(3.9))  # 60.31143162393162
print(liters_100km_to_miles_gallon(7.5))  # 31.36194444444444
print(liters_100km_to_miles_gallon(10.))  # 23.52145833333333
print(miles_gallon_to_liters_100km(60.3)) # 3.900739358761747
print(miles_gallon_to_liters_100km(31.4)) # 7.490910297239915
print(miles_gallon_to_liters_100km(23.5)) # 10.009131205673757
