def runLengthEncoding(string):
    # Write your code here.
    newList = list(string)
	newList.append(float('inf'))
	n = len(newList)
	updatedList = []
	curCount = 0
	prev = newList[0]
	for cur in newList:
		if curCount == 9:
			updatedList.append(str(9))
			updatedList.append(prev)
			curCount = 0
		if cur != prev:
			if curCount != 0:
				updatedList.append(str(curCount))
				updatedList.append(prev)
			prev = cur
			curCount = 1
		else:
			curCount += 1
	returnString = ''.join(updatedList)
	return returnString
		
