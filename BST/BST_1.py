#praveen kumar
#Indian institute of information technology kalyani (W.B)


class Node:
        def __init__(self,data):
                self.data=data
                self.leftchild=None
                self.rightchild=None


class BinarySearchTree:
        def __init__(self):
                self.root=None

        #O(logN).....In balanced binary tree like AVL or RED BLACK tree and O(N^2)in Unbalanced binary tree  
        def InsertNode(self,data,node):
                if data<node.data:
                        if node.leftchild is not None:
                                self.InsertNode(data,node.leftchild)
                        else:
                                node.leftchild=Node(data) 

                else:
                        if node.rightchild is not None:
                                self.InsertNode(data,node.rightchild)
                        else:
                                node.rightchild=Node(data)

        def Insert(self,data):
                if self.root is None:
                        self.root=Node(data)
                else:
                        self.InsertNode(data,self.root)



        def getMinValue(self):
                if self.root is not None:
                        return self.getMin(self.root)
        def getMin(self,node):
                if node.leftchild is not None:
                        return self.getMin(node.leftchild)
                return node.data
        def getMaxValue(self):
                if self.root is not None:
                        return self.getMax(self.root)

        def getMax(self,temp):
                if temp.rightchild is not None:
                        return self.getMax(temp.rightchild)
                return temp.data
        def traverseInorder(self,node):
                if node.leftchild is not None:
                        self.traverseInorder(node.leftchild)

                print("%s"%node.data)

                if node.rightchild is not None:
                        self.traverseInorder(node.rightchild)


        def traverse(self):
                if self.root is not None:
                        return self.traverseInorder(self.root)

        def removeNode(self,data,node):
                if node.data is None:
                        return node
                if data<node.data:
                        node.leftchild=self.removeNode(data,node.leftchild)

                elif data>node.data:
                        node.rightchild=self.removeNode(data,node.rightchild)

                else:

                        if node.leftchild is None and node.rightchild is None:
                                print("we are removing leaf node having data:",node.data)
                                del node
                                return None
                        if node.leftchild is None:

                                tempNode=node.rightchild;
                                print("single right node is deleted:",node.data)
                                del node
                                return tempNode
                        elif node.rightchild is None:
                                
                                print(" Single left node is deleted and the node is to be deleted is :",node.data)
                                tempNode=node.leftchild;
                                del node
                                return tempNode

                        
                        print("Removing node with two children :")
                        tempNode=self.getPredecessor(node.leftchild)
                        node.data=tempNode.data
                        node.leftchild=self.removeNode(tempNode.data,node.leftchild)

                return node

        #Here we can also prefer succussor insted of precedessor
        def getPredecessor(self,node):
                if node.rightchild is not None:
                        return self.getPredecessor(node.rightchild)
                return node
        #o(logN)...for deletion in binary tree (Best case) and o(N^2)in worst case
        def remove(self,data):
                if self.root is not None:
                        self.root=self.removeNode(data,self.root)
        




if __name__=="__main__":
        bst=BinarySearchTree()
        bst.Insert(4)
        bst.Insert(45)
        bst.Insert(8)
        bst.Insert(23) 
        bst.Insert(70)
        print("Min value of the tree",bst.getMinValue())
        print("right most value of tree",bst.getMaxValue())
        print('Inorder traversal after insertion:')
        bst.traverse()
        print(bst.remove(8))
        bst.Insert(9)
        bst.Insert(10)
        bst.Insert(3)
        print("After deletion , Inorder traversal of tree is : ")
        bst.traverse()

                
                        
                
                        
                 
                 
        
