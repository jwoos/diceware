f = open('wordlist.txt', 'r').read()
a = f.split('\n')

the_dict = {
}
for x in a:
	y = x.split('\t')
	if len(y) == 1:
		pass
	else:
		the_dict[y[0]] = y[1]

print(the_dict)
