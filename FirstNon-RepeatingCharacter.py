def firstNonRepeatingCharacter(string):
	characterDict = {}
	for character in string:
		if character not in characterDict:
			characterDict[character] = 1
		else:
			characterDict[character] += 1
			
	for i in range(len(string)):
		if characterDict[string[i]] == 1:
			return i
	return -1
