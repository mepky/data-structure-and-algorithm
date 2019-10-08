class newNode:
	def __init__(self,data):
		self.val=data
		self.left=None 
		self.right=None
		self.visited=False

def postorder(temp):
	root=temp

	while (root and root.visited==False):

		if (root.left and root.left.visited==False):
			root=root.left

		elif (root.right and root.right.visited==False):
			root=root.right

		else:
			print(root.val,end=' ')
			root.visited=True
			temp=root
			


root = newNode(8)  
root.left = newNode(3)  
root.right = newNode(10)  
root.left.left = newNode(1)  
root.left.right = newNode(6)  
root.left.right.left = newNode(4)  
root.left.right.right = newNode(7)  
root.right.right = newNode(14)  
root.right.right.left = newNode(13)  
postorder(root) 