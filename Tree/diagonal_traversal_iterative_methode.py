class Node:
	def __init__(self,data):
		self.val=data
		self.left=None
		self.right=None
#Function to print diagonal view
def diagonalprint(root):
	#base case
	if root is None:
		return 
# queue of treenode
	q=[]
	#Append root
	q.append(root)
	#Append delimiter
	q.append(None)

	while len(q)>0:
		temp=q.pop(0)
		#If current is delimiter then insert another 
		#for next diagonal and cout nextline
		if not temp:
			#If queue is empty then return 
			if len(q)==0:
				return 
				#Print output on nextline
			print(' ')
			#append delimiter again 
			q.append(None)

		else:
			while temp:
				print(temp.val,end=' ')
				#If left child is present
				#append into queue
				if temp.left:
					q.append(temp.left)
				#current equals to right child
				temp=temp.right

root = Node(8) 
root.left = Node(3) 
root.right = Node(10) 
root.left.left = Node(1) 
root.left.right = Node(6) 
root.right.right = Node(14) 
root.right.right.left = Node(13) 
root.left.right.left = Node(4) 
root.left.right.right = Node(7) 
print('Diagonal Traversal of tree is :')  
diagonalprint(root) 