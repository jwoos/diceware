import sys
from random import SystemRandom

length = int(sys.argv[1])
digits = []

random_dig = SystemRandom()

for word in range(length):
	this_word = ''
	for dig in range(5):
		a_dig = random_dig.randrange(1, 7)
		this_word += str(a_dig)
	digits.append(int(this_word))

print(digits)
