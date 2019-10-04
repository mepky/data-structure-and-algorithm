class Node:
	def __init__(self,data):
		self.val=data
		self.left=None
		self.right=None

# Here is two method two solve this question one is given below and another one 
# is given below.below 
'''

def height(root):
	if root is None:
		return 0
	else:

		lheight=height(root.left)
		rheight=height(root.right)

		if lheight>rheight:
			return lheight+1
		else:
			return rheight+1

def givenlevelorder(root,level):
	if root is None:
		return 

	if level==1:
		print(root.val,end=' ')
	elif level>1:
		givenlevelorder(root.left,level-1)
		givenlevelorder(root.right,level-1)

def printlevelorder(root):
	h=height(root)
	for i in range(h,0,-1):
		givenlevelorder(root,i)

'''
def reverse_level_order(root):
	q=[]
	s=[]
	q.append(root)

	while len(q)>0:
		root=q.pop(0)
		s.append(root)

		if root.right:
			q.append(root.right)

		if root.left:
			q.append(root.left)

	while len(s)>0:
		root=s.pop()
		print(root.val,end=' ')




root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 
  
print("Level Order traversal of binary tree is")
reverse_level_order(root) 
 #print("Level Order traversal of binary tree is")
#printlevelorder(root) 

#This code is contributed by Praveen kumar (IIIT Kalyani)
# o(n**2) 