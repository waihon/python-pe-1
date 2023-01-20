# Store the current largest number here.
largest_number = -999_999_999

# Input the first value
number = int(input("Enter a number of type -1 to stop: "))

# If the number is not equal to -1, coninue.
while number != -1:
    # Is number larger than largest_number?
    if number > largest_number:
        # Yes, update largest_number.
        largest_number = number
    # Input the next number
    number = int(input("Enter a number of type -1 to stop: "))

# Print the largest number.
print("The largest number is: ", largest_number)
