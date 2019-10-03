class Node:
	def __init__(self,data):
		self.val=data
		self.left=None
		self.right=None


#k=height(root)
l=[0]*4
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
		#l[j].extend(root.val)
		print(root.val,end=' ')
		print('\n',end=' ')
		

	elif level>1:
		givenlevel(root.left,level-1)
		givenlevel(root.right,level-1)

def printlevelorder(root):
	h=height(root)
	for i in range(1,h+1):
		
		givenlevel(root,i)

root = Node(1); 
root.left = Node(2); 
root.right = Node(3); 
root.left.left = Node(4); 
root.left.right = Node(5); 
root.right.right = Node(6); 
  
printlevelorder(root)
#print(l)