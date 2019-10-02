class getNode: 
    def __init__(self, data): 
          
        # put in the data  
        self.data = data  
        self.left = self.right = None
      
# function to store the inorder traversal  
# of the binary tree in 'arr'  
def storeInorderTraversal(root, arr): 
      
    # if root is None  
    if (not root): 
        return
  
    # first recur on left child  
    storeInorderTraversal(root.left, arr)  
  
    # then store the root's data in 'arr'  
    arr.append(root.data)  
  
    # now recur on right child  
    storeInorderTraversal(root.right, arr) 
  
# function to replace each node with the  
# sum of its inorder predecessor and successor  
def replaceNodeWithSum(root, arr, i): 
      
    # if root is None  
    if (not root): 
        return
  
    # first recur on left child  
    replaceNodeWithSum(root.left, arr, i)  
  
    # replace node's data with the sum of its  
    # inorder predecessor and successor  
    root.data = arr[i[0] - 1] + arr[i[0] + 1]  
  
    # move 'i' to poto the next 'arr' element  
    i[0] += 1
  
    # now recur on right child  
    replaceNodeWithSum(root.right, arr, i) 
  
# Utility function to replace each node in  
# binary tree with the sum of its inorder   
# predecessor and successor  
def replaceNodeWithSumUtil(root): 
      
    # if tree is empty  
    if (not root):  
        return
  
    arr = []  
  
    # store the value of inorder predecessor  
    # for the leftmost leaf  
    arr.append(0)  
  
    # store the inoder traversal of the 
    # tree in 'arr'  
    storeInorderTraversal(root, arr)  
  
    # store the value of inorder successor  
    # for the rightmost leaf  
    arr.append(0)  
  
    # replace each node with the required sum  
    i = [1] 
    replaceNodeWithSum(root, arr, i) 
  
# function to prthe preorder traversal  
# of a binary tree  
def preorderTraversal(root): 
      
    # if root is None  
    if (not root):  
        return
  
    # first prthe data of node  
    print(root.data, end = " ") 
  
    # then recur on left subtree  
    preorderTraversal(root.left)  
  
    # now recur on right subtree  
    preorderTraversal(root.right) 
  
# Driver Code 
if __name__ == '__main__': 
      
    # binary tree formation  
    root = getNode(1) #         1      
    root.left = getNode(2)     #     / \      
    root.right = getNode(3)     #     2     3      
    root.left.left = getNode(4) # / \ / \  
    root.left.right = getNode(5) # 4 5 6 7  
    root.right.left = getNode(6)  
    root.right.right = getNode(7)  
  
    print("Preorder Traversal before",  
                 "tree modification:")  
    preorderTraversal(root)  
  
    replaceNodeWithSumUtil(root)  
    print() 
    print("Preorder Traversal after",  
                "tree modification:")  
    preorderTraversal(root) 
  