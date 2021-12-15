def findThreeLargestNumbers(array):
    # Write your code here.
    max1 = float('-inf')
	max2 = float('-inf')
	max3 = float('-inf')
	
	for i in array:
		if i >= max1:
			max3 = max2
			max2 = max1
			max1 = i
		elif i >= max2:
			max3 = max2
			max2 = i
		elif i >= max3:
			max3 = i
	maxArray = []
	maxArray.append(max3)
	maxArray.append(max2)
	maxArray.append(max1)
	return maxArray
