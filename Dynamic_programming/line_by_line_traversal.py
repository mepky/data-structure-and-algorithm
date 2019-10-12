class newNode:
	def __init__(self,data):
		self.val=data
		self.left=None
		self.right=None

def printLevelOrder(root):
	if root is None:
		return

	q=[]
	q.append(root)

	while q:
		count=len(q)
		while count>0:
			temp=q.pop(0)
			print(temp.val,end=' ')
			if temp.left:
				q.append(temp.left)
			if temp.right:
				q.append(temp.right)

			count-=1
		print(' ')
root = newNode(1); 
root.left = newNode(2); 
root.right = newNode(3); 
root.left.left = newNode(4); 
root.left.right = newNode(5); 
root.right.right = newNode(6); 
 
printLevelOrder(root);