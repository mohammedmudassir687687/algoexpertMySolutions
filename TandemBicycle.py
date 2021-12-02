def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
	if len(redShirtSpeeds) == 0:
		return 0
	
	redShirtSpeeds.sort()
	blueShirtSpeeds.sort(reverse=True)
	totalSpeed = 0
	n = len(redShirtSpeeds)
	if fastest:
		for i in range(n):
			totalSpeed += max(redShirtSpeeds[i], blueShirtSpeeds[i])
	else:
		blueShirtSpeeds.sort()
		for i in range(n):
			totalSpeed += max(redShirtSpeeds[i], blueShirtSpeeds[i])
			
	return totalSpeed
