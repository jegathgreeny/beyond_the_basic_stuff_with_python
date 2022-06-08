def a():
	print('Start of a')
	b()

def b():
	print('Start of b')
	c()

def c():
	print('Start of c')
	# This will cause a zero division error.
	44/0

a()