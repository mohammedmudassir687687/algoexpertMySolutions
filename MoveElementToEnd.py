def moveElementToEnd(array, toMove):
    # Write your code here.
    insertLocation = 0
	toMoveCount = 0
	i = 0
	while i < len(array):
		if array[i] == toMove:
			toMoveCount += 1
		else:
			array[insertLocation] = array[i]
			insertLocation += 1
		i += 1
		
	while toMoveCount > 0:
		array[insertLocation] = toMove
		toMoveCount -= 1
		insertLocation += 1
	return array
