def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

def heron(a, b, c):
    s = (a + b + c) / 2 # semi-perimeter
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

def area_of_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    return heron(a, b, c)

if __name__ == "__main__":
    print(area_of_triangle(1., 1., 2. ** .5)) # ~0.5
    print(area_of_triangle(3., 4., 5.)) # 6.0
