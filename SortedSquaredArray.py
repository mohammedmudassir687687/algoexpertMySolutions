def sortedSquaredArray(array):
    # Write your code here.
	n = len(array)
    if array == []:
		return []
	newArray = []
	positive, negative = n, -1
	for i in range(n):
		if array[i] > 0:
			positive = i
			break
	for i in range(n-1, -1, -1):
		if array[i] < 0:
			negative = i
			break
			
	positiveFlag, negativeFlag = False, False
	while negative > -1 or positive < n:
		if negative == -1:
			negativeFlag = True
		if positive == n:
			positiveFlag = True
		if negativeFlag and positiveFlag:
			break
		if negativeFlag == True or positiveFlag == False and array[positive] < -1*array[negative]:
			newArray.append(array[positive] * array[positive])
			positive += 1
		elif positiveFlag == True or negativeFlag == False and array[positive] > -1*array[negative]:
			newArray.append(array[negative] * array[negative])
			negative -= 1
		elif array[positive] == -1*array[negative]:
			newArray.append(array[positive] * array[positive])
			positive += 1
			
	for i in array:
		if i == 0:
			newArray.insert(0,0)
	return newArray
	
