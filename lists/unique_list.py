my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
temp_list = []

for i in my_list:
    if i not in temp_list:
        temp_list.append(i)

my_list = temp_list
del temp_list
print("The list with unique elements only:")
print(my_list)  # [1, 2, 4, 6, 9]
