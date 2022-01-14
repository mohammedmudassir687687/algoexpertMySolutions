def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    returnArray = []
	arrayOne.sort()
	arrayTwo.sort()
	curDifference = float("inf")
	n = len(arrayOne)
	m = len(arrayTwo)
	if n <= m:
		iterationSize = n
	else:
		iterationSize = m
	i = 0
	j = 0
	indexReturnI = 0
	indexReturnJ = 0
	while i < n or j < m:
		newDifference = abs(arrayOne[i] - arrayTwo[j])
		if curDifference > newDifference:
			curDifference = newDifference
			indexReturnI = i
			indexReturnJ = j
		if arrayOne[i] == arrayTwo[j]:
			break
		elif arrayOne[i] < arrayTwo[j]:
			if i+1 < n:
				i += 1
			else:
				break
		else:
			if j+1 < m:
				j += 1
			else:
				break
		
	returnArray.append(arrayOne[indexReturnI])
	returnArray.append(arrayTwo[indexReturnJ])
	return returnArray
 
