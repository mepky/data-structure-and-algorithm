class Node:
	def __init__(self,data):
		self.val=data
		self.left=None
		self.right=None

def Morris_Traversal(root):
	cur=root

	while cur:

		if cur.left is None:
			print(cur.val,end=' ')
			cur=cur.right
		else:
			prev=cur.left

			while prev.right is not None and prev.right !=cur:
				prev=prev.right

			if prev.right is cur:
				prev.right=None
				cur=cur.right

			else:
				print(cur.val,end=' ')
				prev.right=cur
				cur=cur.left


def preorder(root):
	if root:
		print(root.val,end=' ')
		preorder(root.left)
		preorder(root.right)
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
  
root.left.left = Node(4) 
root.left.right = Node(5) 
  
root.right.left= Node(6) 
root.right.right = Node(7) 
  
root.left.left.left = Node(8) 
root.left.left.right = Node(9) 
  
root.left.right.left = Node(10) 
root.left.right.right = Node(11) 
  
  
Morris_Traversal(root) 
print("\n") 
preorder(root) 
