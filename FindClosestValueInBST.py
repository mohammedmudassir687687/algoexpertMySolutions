def findClosestValueInBst(tree, target):
    # Write your code here.
	minDifference = abs(target - tree.value)
	value = tree.value
	while True:
		if minDifference == 0:
			return tree.value
		elif target > tree.value and tree.right != None:
			tree = tree.right
			if minDifference > abs(target - tree.value):
				minDifference = abs(target - tree.value)
				value = tree.value
		elif target < tree.value and tree.left != None:
			tree = tree.left
			if minDifference > abs(target - tree.value):
				minDifference = abs(target - tree.value)
				value = tree.value
		else:
			break
	return value
# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
