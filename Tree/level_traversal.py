#Print level order traversal line by line | Set 1
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

def givenlevel(root,level,j):
	if root is None:
		return None
	
	if level==1:
		#print(root.val,end=' ')
		l[j].extend([root.val])
		

	elif level>1:
		givenlevel(root.left,level-1,j)
		givenlevel(root.right,level-1,j)

	
def printlevelorder(root):
	h=height(root)
	for i in range(1,h+1):
		givenlevel(root,i,i-1)

def line_by_line(l):
	for i in range(len(l)):
		for j in range(len(l[i])):
			print(l[i][j],end=' ')
		print(' ')


if __name__=='__main__':
	root = Node(1) 
	root.left=Node(2)
	root.right = Node(3) 
	root.left.left = Node(4) 
	root.left.right = Node(5) 
	root.right.right=Node(6)
	h=height(root)
	l=[[] for _ in range(h)]
	print("Level order traversal of binary tree is -")

	printlevelorder(root)
	line_by_line(l)
