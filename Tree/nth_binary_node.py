#Indian institute of information technology kalyani W.B

class Node:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

count=[0]

def inorder(root,n):
	if not root:
		return 

	if count[0]<=n:
		inorder(root.left,n)
		count[0]+=1

		if count[0]==n:
			print(root.data,end=' ')

		inorder(root.right,n)

if __name__ == '__main__': 
  
    root = Node(10)  
    root.left = Node(20)  
    root.right = Node(30)  
    root.left.left = Node(40)  
    root.left.right = Node(50)  
  
    n = 4
  
    inorder(root, n) 
