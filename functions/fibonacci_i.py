def fibonacci(n):
    # fib_1 = 1
    # fib_2 = 1
    # fib_i = fib_i-1 + fib_i-2
    if n < 1:
        return None
    if n < 3:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)

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
