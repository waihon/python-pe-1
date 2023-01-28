def bmi(weight, height):
    # Valid weight is between infant's and that of heaviest man ever.
    # Valid height is between infant's and that of tallest man ever.
    if weight < 3.0 or weight > 640.0 or \
    height < 0.45 or height > 2.8:
        return None

    return weight / height ** 2

def lb_to_kg(lb):
    return lb * 0.45359237

if __name__ == "__main__":
    print(bmi(70.0, 1.58))  # 28.040378144528116
    print(bmi(641.0, 1.65)) # None
    print(lb_to_kg(100))    # 45.359237
