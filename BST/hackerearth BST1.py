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
            root.right=node
        else:
            insert(root.right,node)
    else:
        if root.left is None:
            root.left=node
        else:
            insert(root.left,node)
            
def inorder(root):
        if root:
                inorder(root.left)
                print(root.data)
                inorder(root.right)

n=int(input())
l=list(map(int,input().split(' ')))
root=Node(l[0])
for i in range(1,n):
    insert(root,Node(l[i]))


def maxdepth(root):
        if root is None:
                return 0
        else:
                ldepth=maxdepth(root.left)
                rdepth=maxdepth(root.right)

        if ldepth>rdepth:
                return ldepth+1
        else:
                return rdepth+1


#inorder(root)
print(maxdepth(root))
    
 
