def caesarCipherEncryptor(string, key):
    # Write your code here.
	listString = list(string)
    for i in range(len(listString)):
		if ord(listString[i]) + key > 97 + 25:
			diff = 97+25 - ord(listString[i])
			remain = key - diff
			remain = remain%26
			listString[i] = chr(97 + remain - 1)
		else:
			listString[i] = chr(ord(listString[i]) + key)
	return ''.join(listString)
 
