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

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "-> ", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
	else:
        print("Failed")
