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

f = open('wordlist.txt', 'r').read()
a = f.split('\n')

the_dict = {}

for x in a:
	y = x.split('\t')
	if len(y) == 1:
		pass
	else:
		the_dict[y[0]] = y[1]

for dig in digits:
	print(dig, end ='\t')
print('')

for dig in digits:
	print(the_dict[str(dig)], end='\t')
print('')
