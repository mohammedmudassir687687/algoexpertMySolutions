# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array, depth = 1):
    # Write your code here.
	total = 0
	n = len(array)
	i = 0
	while i < n:
		if type(array[i]) is list:
			total += depth * productSum(array[i], depth + 1)
		else:
			total += array[i] * depth
		i += 1
	return total
			
