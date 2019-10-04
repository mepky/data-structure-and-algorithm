class Node:
	def __init__(self,data):
		self.val=data
		self.left=None
		self.right=None

def specific(root):

	if not root:
		return 

	
	print(root.val,end=' ')

	if root.left:
		print(root.left.val,end=' ')
		print(root.right.val,end=' ')

	if root.left.left is None:
		return 


	q=[]
	q.append(root.left)
	q.append(root.right)

	first=None
	second=None


	while len(q)>0:
		first=q.pop(0)
		second=q.pop(0)

		print(first.left.val,end=' ')
		print(second.right.val,end=' ')
		print(first.right.val,end=' ')
		print(second.left.val,end=' ')

		if first.left.left is not None:
			q.append(first.left)
			q.append(second.right)
			q.append(first.right)
			q.append(second.left)


root = Node(1) 
   
root.left= Node(2) 
root.right   = Node(3) 
   
root.left.left  = Node(4) 
root.left.right = Node(5) 
root.right.left  = Node(6) 
root.right.right = Node(7) 
   
root.left.left.left  = Node(8) 
root.left.left.right  = Node(9) 
root.left.right.left  = Node(10) 
root.left.right.right  = Node(11) 
root.right.left.left  = Node(12) 
root.right.left.right  = Node(13) 
root.right.right.left  = Node(14) 
root.right.right.right  = Node(15) 
   
root.left.left.left.left  = Node(16) 
root.left.left.left.right  = Node(17) 
root.left.left.right.left  = Node(18) 
root.left.left.right.right  = Node(19) 
root.left.right.left.left  = Node(20) 
root.left.right.left.right  = Node(21) 
root.left.right.right.left  = Node(22) 
root.left.right.right.right  = Node(23) 
root.right.left.left.left  = Node(24) 
root.right.left.left.right  = Node(25) 
root.right.left.right.left  = Node(26) 
root.right.left.right.right  = Node(27) 
root.right.right.left.left  = Node(28) 
root.right.right.left.right  = Node(29) 
root.right.right.right.left  = Node(30) 
root.right.right.right.right  = Node(31) 
   
print ("Specific Level Order traversal of binary tree is")
specific(root); 
   

