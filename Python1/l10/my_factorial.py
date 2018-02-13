def lavash_factorial(number):
	i = 1
	result = 1
	while i <= number:
		result *= i
		i += 1
	return result

print(lavash_factorial(5))