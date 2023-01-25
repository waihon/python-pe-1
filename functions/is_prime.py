def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    
    max_divisor = num // 2 + 1
    for div in range(2, max_divisor + 1):
        if num % div == 0:
            return False
    return True

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()
