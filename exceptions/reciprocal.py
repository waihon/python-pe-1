try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)
except ValueError:
    print('I do not know what to do.')
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.')
except:
    print('Something strange has happened here... Sorry!')

"""
Enter a natural number: 4
The reciprocal of 4 is 0.25
Enter a natural number: four
I do not know what to do.
Enter a natural number: 0
Division by zero is not allowed in our Universe.
"""
