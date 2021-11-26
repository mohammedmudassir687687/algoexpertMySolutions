def tournamentWinner(competitions, results):
    # Write your code here.
    # have to maintain a scores dictionary for teams of size k
	# 0 means second team won, 1 means first team won
	# loop O(n) - if 0 take competitions[1], else competitions[0]
	# max score of the dictionary then return that team name
	
	scores = {}
	for i in competitions:
		if i[0] not in scores.keys():
			scores[i[0]] = 0
		if i[1] not in scores.keys():
			scores[i[1]] = 0
			
	n = len(results)
	
	for i in range(n):
		if results[i] == 0:
			scores[competitions[i][1]] += 1
		else:
			scores[competitions[i][0]] += 1
			
	winningScore = max(scores.values())
	for i,j in scores.items():
		if j == winningScore:
			return i
