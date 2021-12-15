def binarySearch(array, target):
    # Write your code here.
	n = len(array)
	low = 0
	high = n-1
	
	while low <= high:
		mid = (low + high) // 2
		if target == array[mid]:
			return mid
		elif target < array[mid]:
			high = mid - 1
		elif target > array[mid]:
			low = mid + 1
	
	return -1
