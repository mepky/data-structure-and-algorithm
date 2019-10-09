class Node:
	def __init__(self,data):
		self.val=data
		self.left=None
		self.right=None


def printdiagonalutil(root,d,diagonalprintmap):
	if root is None:
		return 

	try:
		diagonalprintmap[d].append(root.val)
	except KeyError:
		diagonalprintmap[d]=[root.val]


	printdiagonalutil(root.left,d+1,diagonalprintmap)
	printdiagonalutil(root.right,d,diagonalprintmap)


def printdiagonal(root):
	diagonalprintmap=dict()
	printdiagonalutil(root,0,diagonalprintmap)

	print('Diagonal Traversal of binary tree: ')
	for i in diagonalprintmap:
		for j in diagonalprintmap[i]:
			print(j,end=' ')
		print(' ')


root = Node(8) 
root.left = Node(3) 
root.right = Node(10) 
root.left.left = Node(1) 
root.left.right = Node(6) 
root.right.right = Node(14) 
root.right.right.left = Node(13) 
root.left.right.left = Node(4) 
root.left.right.right = Node(7) 
  
printdiagonal(root) 