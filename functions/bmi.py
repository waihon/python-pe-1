def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None

    return weight / height ** 2

if __name__ == "__main__":
    print(bmi(70.0, 1.58))  # 28.040378144528116
    print(bmi(352.5, 1.65)) # None
