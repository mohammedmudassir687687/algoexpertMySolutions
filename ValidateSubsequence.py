def isValidSubsequence(array, sequence):
    # Write your code here.
    if len(sequence) == 0:
		return False
	
	count = 0
	i, j = 0, 0
	while i < len(sequence) and j < len(array):
		if sequence[i] == array[j]:
			i += 1
			j += 1
			count += 1
		else:
			j += 1
			
	if count == len(sequence):
		return True
	else:
		return False
			
