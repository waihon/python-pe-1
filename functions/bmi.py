def bmi(weight, height):
    # Valid weight is between infant's and that of heaviest man ever.
    # Valid height is between infant's and that of tallest man ever.
    if weight < 3.0 or weight > 640.0 or \
    height < 0.45 or height > 2.8:
        return None

    return weight / height ** 2

def lb_to_kg(lb):
    return lb * 0.45359237
    
def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254 # (2.54 cm)

if __name__ == "__main__":
    print(bmi(70.0, 1.58))  # 28.040378144528116
    print(bmi(641.0, 1.65)) # None
    print(lb_to_kg(100))    # 45.359237
    print(ft_and_inch_to_m(5, 7)) # 1.7018
    print(ft_and_inch_to_m(6, 0)) # 1.8288000000000002
    print(ft_and_inch_to_m(6))    # 1.8288000000000002
