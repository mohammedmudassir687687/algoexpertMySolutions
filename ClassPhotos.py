def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
	if len(redShirtHeights) == 1:
		if redShirtHeights[0] == blueShirtHeights[0]:
			return False
		else:
			return True
	n = len(redShirtHeights)
	redShirtHeights.sort()
	blueShirtHeights.sort()
	
	if redShirtHeights[0] == blueShirtHeights[0]:
		return False
	elif redShirtHeights[0] > blueShirtHeights[0]:
		backRow = 'red'
	else:
		backRow = 'blue'
		
	if backRow == 'red':
		for i in range(n):
			if redShirtHeights[i] > blueShirtHeights[i]:
				continue
			else:
				return False
		return True
	else:
		for i in range(n):
			if redShirtHeights[i] < blueShirtHeights[i]:
				continue
			else:
				return False
		return True
	
