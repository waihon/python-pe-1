starting_hours = int(input("Starting time (hours): "))
starting_minutes = int(input("Starting time (minutes): "))
duration_in_minutes = int(input("Event duration (minutes): "))

minutes = (starting_minutes + duration_in_minutes) % 60
additional_hours = (starting_minutes + duration_in_minutes) // 60
hours = (starting_hours + additional_hours) % 24

print(hours, ":", minutes, sep="")

"""
Starting time (hours): 12
Starting time (minutes): 17
Event duration (minutes): 59
13:16
Starting time (hours): 23
Starting time (minutes): 58
Event duration (minutes): 642
10:40
Starting time (hours): 0
Starting time (minutes): 1
Event duration (minutes): 2939
1:0
"""
