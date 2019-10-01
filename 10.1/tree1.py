def postorder(inorder,preorder,n):
	if preorder[0] in inorder:
		root=inorder.index(preorder[0])

	if root!=0:
		postorder(inorder[:root],preorder[1:root+1],len(inorder[:root]))

	if root !=n-1:
		postorder(inorder[root+1:],preorder[root+1:],len(inorder[root+1:]))

	print(preorder[0],end=' ')


inorder = [4, 2, 5, 1, 3, 6]; 
preorder = [1, 2, 4, 5, 3, 6]; 
n = len(inorder) 
print("Postorder traversal ")
postorder(inorder, preorder, n) 
  
