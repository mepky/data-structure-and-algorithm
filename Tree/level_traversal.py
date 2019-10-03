class Node:
	def __init__(self,data):
		self.val=data
		self.left=None
		self.right=None

def height(root):
	if root is None:
		return 0
	else:

		#Height of each subtree
		lheight=height(root.left)
		rheight=height(root.right)

		if lheight>rheight:
			return lheight+1
		else:
			return rheight+1

def givenlevel(root,level):
	if root is None:
		return None

	if level==1:
		print(root.val,end=' ')
		

	elif level>1:
		givenlevel(root.left,level-1)
		givenlevel(root.right,level-1)

def printlevelorder(root):
	h=height(root)
	for i in range(1,h+1):
		givenlevel(root,i)

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
  
print("Level order traversal of binary tree is -")
printlevelorder(root) 