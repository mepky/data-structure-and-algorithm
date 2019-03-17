class Node:
        def __init__(self,data):
                self.data=data
                self.right=None
                self.left=None

def insert(root,node):
        if root is None:
                root=node

        if root.data<node.data:
                if root.right is None:
                        root.right =node
                else:
                        insert(root.right,node)
                        
        else:
                if root.left is None:
                        root.left=node
                else:
                        insert(root.left,node)


def preorder(node):
        if node is not None:
                print(node.data)
                preorder(node.left)
                preorder(node.right)

def inorder(node):
        if node :
                inorder(node.left)
                print(node.data)
                inorder(node.right)
                
                
        
        
        



n=int(input())
n1=list(map(int,input().split(' ')))
q=int(input())
root=Node(n1[0])
for i in range(1,n):
        insert(root,Node(n1[i]))
#preorder(Node(q))
inorder(root)

        
