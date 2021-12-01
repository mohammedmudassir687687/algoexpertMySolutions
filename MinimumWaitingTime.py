def minimumWaitingTime(queries):
    # Write your code here.
	queries.sort()
	n = len(queries)
	minWaitingTime = 0
	prev = 0
	for i in range(n):
		minWaitingTime += prev
		prev += queries[i]
	
    return minWaitingTime
