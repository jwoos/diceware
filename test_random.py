from random import SystemRandom

numbers = {}

for _ in range(6000):
	random_dig = SystemRandom()
	a_dig = random_dig.randrange(1, 7)
	if a_dig not in numbers:
		numbers[a_dig] = 0
	elif a_dig in numbers:
		numbers[a_dig] += 1

print(numbers)
