def calcNodeDepths(depth, root):
	if root == None:
		return 0
	return depth + calcNodeDepths(depth + 1, root.left) + calcNodeDepths(depth + 1, root.right)


def nodeDepths(root):
    # Write your code here.
	depth = 0
	if root == None:
		return 0
	return calcNodeDepths(depth, root)
	
	

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
