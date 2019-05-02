def fibnaughty():
	n = input('The amount of numbers in the sequence')
	a,b = 0,1
	while a < n:
		print a
		a,b = b, a+b
		