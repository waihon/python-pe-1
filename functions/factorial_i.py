def factorial(n):
    if n < 0:
        return None
    if n < 2:
        return 1

    product = 1
    for i in range(2, n+1):
        product *= i

    return product

if __name__ == "__main__":
    for n in range(-1, 6):
        print(n, factorial(n))
    """
    -1 None
    0 1
    1 1
    2 2
    3 6
    4 24
    5 120
    """
