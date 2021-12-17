def generateDocument(characters, document):
    # Write your code here.
	if document == "":
		return True
    characterDict = {}
	for character in characters:
		if character in characterDict:
			characterDict[character] += 1
		else:
			characterDict[character] = 1
			
	for character in document:
		if character not in characterDict:
			return False
		elif characterDict[character] == 0:
			return False
		else:
			characterDict[character] -= 1
	return True
