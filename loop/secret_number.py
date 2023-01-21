secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

while True:
    guess = int(input("Enter a number: "))
    if guess != secret_number:
        print("Ha ha! Your're stuck in my loop!")
    else:
        print("Well done, muggle! You are free now.")
        break
