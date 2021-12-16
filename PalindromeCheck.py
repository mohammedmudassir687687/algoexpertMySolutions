def isPalindrome(string):
    # Write your code here.
    i = 0
	n = len(string)
	j = n - 1
	flag = True
	while i <= j:
		if string[i] != string[j]:
			return False
		i += 1
		j -= 1
	return True
