def factorial(n):
    # 0! = 1
    # 1! = 1
    # n! = 1 x 2 x 3 x ... x n-1 x n
    #    = (n-1)! x n
    if n < 0:
        return None
    if n < 2: # the base case (termination condition)
        return 1

    return factorial(n-1) * n

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
