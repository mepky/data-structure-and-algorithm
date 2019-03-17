t=int(input())
for i in range(t):
        n,x=map(int,input().split(' '))
        n=int(n)
        x=int(x)
        l=list(map(int,input().split(' ')))

        class Node:
                def __init__(self,data):
                        self.data=data
                        self.left=None
                        self.right=None

        def insert(root,node):
                if root is None:
                        root=node
                else:
                        if root.data>node.data:
                                if root.left is None:
                                        root.left=node
                                else:
                                        insert(root.left,node)
                        if root.data <node.data:
                                if root.right is None:
                                        root.right=node
                                else:
                                        insert(root.right,node)
        def inorder(node):
                if node:
                        inorder(node.left)
                        print(node.data)
                        inorder(node.right)

        root=Node(l[0])
        for i in range(1,n):
                insert(root,Node(i))
        inorder(root)



















                        
