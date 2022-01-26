def isMonotonic(array):
    # Write your code here.
    decreasing = False
	increasing = False

	for i in range(1, len(array)):
		if array[i] == array[i-1]:
			continue
		elif array[i] > array[i-1]:
			increasing = True
		else:
			decreasing = True
			
		if increasing and decreasing:
			return False;
	return True;
