# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



def recurSum(total, root, returnArr):
	total += root.value
	if root.left == None and root.right == None:
		returnArr.append(total)
	if root.left != None:
		recurSum(total, root.left, returnArr)
	if root.right != None:
		recurSum(total, root.right, returnArr)
	return returnArr

def branchSums(root):
    # Write your code here.
	returnArr = []
	if root == None:
		return []
    total = 0
	returnArray = recurSum(total, root, returnArr)
	
	return returnArray
	
	
