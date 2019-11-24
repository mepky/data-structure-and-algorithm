#Given inorder traversal of tree

def build_tree(l):
	if l is None:
		return 
	max_val=max(l)
	max_index=l.index(max_val)
	root=TreeNode(max_val)
	root.left=build_tree([:max_index])
	root.right=build_tree([max_index+1:])

	return root

#Convert sorted array to binary search tree
def sorted_array_to_bst(A):
	if A==0:
		return 
	if A==1:
		return A
	mid=len(A)//2
	root=TreeNode(A[mid])
	root.left=TreeNode(A[:mid])
	root.right=TreeNode(A[mid+1:])

	return root


#BINARY TREE FROM INORDER TO POSTORDER
#a=inorder_traversal
#b=postorder_traversal
#IN this case first construct right then left got it .
def binary_tree(a,b):
	if not a or not b:
		return None
	idx=a.index(b.pop())
	root=TreeNode(a[idx])
	root.left=binary_tree(a[:idx],b)
	root.right=binary_tree(a[idx+1:],b)

	return root

#BINRAY TREE FROM INORDER AND PREORDER TRAVERSAL
#A=INORDER,B=PREORDER
def binary_tree_i_p(A,B):
	if A is None:
		return 
	idx=A.index(B.[0])
	root=TreeNode(A[idx])
	root.left=binary_tree_i_p(A[1:idx+1],b[:idx])
	root.right=binary_tree_i_p(A[idx+1:],b[idx+1:])

	return root

def kth_smallest(A,k):
	p=inoder(A)
	return p[k+1]
	

	def inorder(A):
		stack=list()
		values=list()
		root=A
		while root:
			if stack.left :
				stack.append(root)
				root=root.left
			elif:
				if len(stack)>0:
					l=stack.pop()
					values.append(l)
					root=root.right
			else:
				return values


def inorder(A):
	stack=list()
	val=list()
	while A:
		if stack:
			stack.append(root)
			root=root.left
		else:
			if len(stack)>0:
				val.append(stack.pop())
				root=root.right
	return val

def findk(A,k):
	l=inorder(A)
	i=0
	j=len(l)-1
	count=0
	while i<j and j<len(l):
		if l[i]+l[j]==k:
			count+=1
			i+=1

		elif l[i]+l[j]<k:
			i+=1
		else:
			j-=1
	return count



