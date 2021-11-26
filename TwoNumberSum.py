def twoNumberSum(array, targetSum):
    # Write your code here.
    tempDict = {}
	for i in array:
		if i not in tempDict.keys():
			tempDict[targetSum - i] = i
		else:
			return [tempDict[i], i]
	return []
