def fibonacci(n):
    # fib_1 = 1
    # fib_2 = 1
    # fib_i = fib_i-1 + fib_i-2
    if n < 1:
        return None
    if n < 3:
        return 1

    fib_i1 = fib_i2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = fib_i1 + fib_i2
        fib_i1, fib_i2 = fib_i2, the_sum

    return the_sum

if __name__ == "__main__":
    for n in (range(-1, 10)):
        print(n, "->", fibonacci(n))
    """
    0 -> None
    1 -> 1
    2 -> 1
    3 -> 2
    4 -> 3
    5 -> 5
    6 -> 8
    7 -> 13
    8 -> 21
    9 -> 34
    """
