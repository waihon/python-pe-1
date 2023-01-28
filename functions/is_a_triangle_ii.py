def is_a_triangle(a, b, c):
    # To form a triangle, the sum of two arbitrary sides
    # (a and b), has to be longer than the third side (c),
    # where (a - b) < c < (a + b).
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True

if __name__ == "__main__":
    print(is_a_triangle(1, 1, 1)) # True
    print(is_a_triangle(3, 4, 5)) # True
    print(is_a_triangle(4, 5, 3)) # True
    print(is_a_triangle(5, 3, 4)) # True
    print(is_a_triangle(1, 1, 3)) # False
    print(is_a_triangle(1, 3, 1)) # False
    print(is_a_triangle(3, 1, 1)) # False
