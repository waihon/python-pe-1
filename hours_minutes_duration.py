# Your task is to prepare a simple code able to evaluate the end time
# of a period of time, given as a number of minutes (it could be
# arbitrarily large). The start time is given as a pair of hours
# (0..23) and minutes (0..59). The result has to be printed to
# the console.

hours    = int(input("Starting time (hours): "))
minutes  = int(input("Starting time (minutes): "))
duration = int(input("Event duration (minutes): "))

# Write your code here.
temp_hours = (minutes + duration) // 60
new_minutes = (minutes + duration) % 60
new_hours = (hours + temp_hours) % 24
print(new_hours, ":", new_minutes, sep="")

"""
Input and expected result:
hours, minutes, duration, end time
12, 17, 59, 13:16
23, 58, 642, 10:40
0, 1, 2939, 1:0
"""
