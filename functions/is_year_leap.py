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

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
	print(yr,"-> ",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
"""
1900 -> OK
2000 -> OK
2016 -> OK
1987 -> OK
"""
