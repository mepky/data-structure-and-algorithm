# INDIAN INSTITUTE OF INFOMATION TECHNOLOGY KALYANI W.B

class Node:
	def __init__(self,data):
		self.val=data
		self.left=None
		self.right=None
'''
def height(root):
	if not root:
		return 0
	else:
		lheight=height(root.left)
		rheight=height(root.right)

		if lheight>rheight:
			return lheight+1
		else:
			return rheight+1

def printspiralorder(root):
	h=height(root)
	t=False
	for i in range(1,h+1):
		givenspiralorder(root,i,t)
		t=(not t)

def givenspiralorder(root,level,t):
	if root is None:
		return
	if level==1:
		print(root.val,end=' ')

	elif level>1:
		if t:
			givenspiralorder(root.left,level-1,t)
			givenspiralorder(root.right,level-1,t)
		else:
			givenspiralorder(root.right,level-1,t)
			givenspiralorder(root.left,level-1,t)


'''
def printspiral(root):
	if root is None:
		return root

	s1=[]#print data from right to left
	s2=[]#print data from left to right

	s1.append(root)
	while  not len(s1)==0 or not len(s2)==0:

		while not len(s1)==0:
			temp=s1[-1]
			s1.pop()
			print(temp.val,end=' ')

			if temp.right:
				s2.append(temp.right)
			if temp.left:
				s2.append(temp.left)

		while not len(s2)==0:
			temp=s2[-1]
			s2.pop()
			print(temp.val,end=' ')

			if temp.left:
				s1.append(temp.left)
			if temp.right:
				s1.append(temp.right)


# Driver Code 
if __name__ == '__main__': 
    root = Node(1)  
    root.left = Node(2)  
    root.right = Node(3)  
    root.left.left = Node(7)  
    root.left.right = Node(6)  
    root.right.left = Node(5)  
    root.right.right = Node(4)  
    print("Spiral Order traversal of binary tree is")  
    #printspiralorder(root) # This method is for recursive printing

    printspiral(root) # Print the iterative method 
      

