while True:
    try:
        number = input("Enter an integer number or Q to exit: ")
        if number == 'Q':
            break
        else:
            number = int(number)
        print("5 divided by", number, "equals", (5 / number), ".")
    except (ValueError, ZeroDivisionError): # parentheses are required
        print("Wrong value or No division by zero rule broken.")
    except:
        print("Sorry, something went wrong...")

"""
Enter an integer number or Q to exit: 3
5 divided by 3 equals 1.6666666666666667 .
Enter an integer number or Q to exit: five
Wrong value or No division by zero rule broken.
Enter an integer number or Q to exit: 0
Wrong value or No division by zero rule broken.
Enter an integer number or Q to exit: Q
"""
