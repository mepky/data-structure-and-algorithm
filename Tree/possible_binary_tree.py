class Node:
	def __init__(self,val):
		self.val=val
		self.left=None
		self.rigth=None



def preorder(root):
	if root:
		print(root.val,end=' ')
		preorder(root.left)
		preorder(root.right)


def gettree(arr,start,end):
	trees=[]
	if start>end:
		trees.append(None)
		return trees

	for i in range(start,end+1):
		lsubtree=gettree(arr,start,i-1)
		rsubtree=gettree(arr,i+1,end)

		for j in lsubtree:
			for k in rsubtree:

				node=Node(arr[i])
				node.left=j
				node.right=k
				trees.append(node)

	return trees

arr=[4,5,7]
n=len(arr)
trees=gettree(arr,0,n-1)
print('Preoder traversal for different binary tree are:')
for i in trees:
	preorder(i)
	print(' ')

