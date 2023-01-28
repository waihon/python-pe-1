def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
    if b > a and b > c:
        return b ** 2 == a ** 2 + c ** 2
    return False

if __name__ == "__main__":
    print(is_a_right_triangle(3, 4, 5)) # True
    print(is_a_right_triangle(4, 5, 3)) # True
    print(is_a_right_triangle(5, 3, 4)) # True
    print(is_a_right_triangle(3, 4, 4)) # False
    print(is_a_right_triangle(3, 5, 5)) # False
