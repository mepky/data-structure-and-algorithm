class Node:
        def __init__(self,data):
                self.data=data
                self.right=None
                self.left=None

def insert(temp,data):
        q=[]
        q.append(temp)
        while(len(q)):
                temp=q[0]
                q.pop(0)
                if (not temp.left):
                        temp.left=Node(data)
                        break
                else:
                        q.append(temp.left)

                if (not temp.right):
                        temp.right=Node(data)
                        break
                else:
                        q.append(temp.right)




#LEVEL ORDER TRAVERSAL_______------

def height(root):
        if root is None:
                return 0
        else:
                lh=height(root.left)
                rh=height(root.right)
        if lh>rh:
                return lh+1
        else:
                return rh+1


def levelorder(root):
        h=height(root)
        for i in range(1,h+1):
                givenlevelorder(root,i)





#Print node at a given lavel
def givenlevelorder(root,level):
        if root is None:
                return None
        if level==1:
                print(root.data)
        if level>1:
                givenlevelorder(root.left,level-1)
                givenlevelorder(root.right,level-1)
                


#--------___________
#DELETION OF NODE IN BINARY TREE------______

def deletenode(root,node):
        q=[]
        q.append(root)
        while(len(q)):
                temp=q[0]
                q.pop(0)
                if (temp.right):
                        if temp.right==node:
                                temp.right=None
                                del node
                                return
                        else:
                                q.append(temp.right)
                
                if temp.left:
                        if temp.left==node:
                                temp.left=None
                                del node
                                return
                        q.append(temp.left)

#Function to delete element in binary tree

def deletion(root,data):
        q=[]
        q.append(root)
        while(len(q)):
                temp=q[0]
                q.pop()
                if temp.data==data:
                        node=temp
                if temp.left:
                        q.append(temp.left)
                if temp.right:
                        q.append(temp.right)


        x=temp.data
        deletenode(root,temp)
        node.data=x


def inorder(temp):
        if (not temp):
                return
        inorder(temp.left)
        print(temp.data)
        inorder(temp.right)



if __name__ == '__main__': 
    root = Node(10)  
    root.left = Node(11)  
    root.left.left = Node(7)  
    root.right = Node(9)  
    root.right.left = Node(15)  
    root.right.right = Node(8)  
  
    print("Inorder traversal before insertion: \n", end = " ") 
    inorder(root)  
  
    key = 12
    insert(root, key)  
  
    print()  
    print("Inorder traversal after insertion:\n", end = " ") 
    inorder(root)

    print('level order traversal :\n')
    levelorder(root)

    print('After deletion of node :\n')
    data=9
    deletion(root,9)
    inorder(root)









                
