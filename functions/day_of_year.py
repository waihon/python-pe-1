def is_year_leap(year):
    if year % 4 != 0:
        # Not divisable by 4, e.g. 1987
        return False
    elif year % 100 != 0:
        # Divisable by 4 but not by 100, e.g. 2016
        return True
    elif year % 400 != 0:
        # Divisable by 100 but not 400, e.g. 1900
        return False
    else:
        # DIvisable by both 100 and 400, e.g. 2000
        return True

def days_in_month(year, month):
    if month < 1 or month > 12:
        return None

    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_year_leap(year):
        days[1] = 29

    return days[month-1]

def day_of_year(year, month, day):
    if month not in list(range(1, 13)) or day not in list(range(1, 32)):
        return None

    result = 0
    for mth in list(range(1, month)): # ignore current month
        result += days_in_month(year, mth)

    result += day # add days of current month
    return result

print(day_of_year(2000, 12, 31)) # 366
print(day_of_year(1987, 12, 31)) # 365
print(day_of_year(2023, 1, 25))  # 25
print(day_of_year(2016, 5, 32))  # None
