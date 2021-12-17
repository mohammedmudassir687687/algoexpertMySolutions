def threeNumberSum(array, targetSum):
    finalArray = []
	array.sort()
	for i in range(len(array) - 2):
		for j in range(i+1, len(array)):
			lastEl = targetSum - array[i] - array[j]
			if lastEl in array[j+1:]:
				finalArray.append([array[i], array[j], lastEl])

	return finalArray
