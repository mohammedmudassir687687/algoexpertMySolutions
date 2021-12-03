def getNthFib(n):
    # Write your code here.
    if n == 1:
		return 0
	elif n == 2:
		return 1
	num = 0
	first = 0
	second = 1
	for i in range(n-2):
		num = second + first
		first = second
		second = num
	return num
