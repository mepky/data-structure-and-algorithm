class Node:
        def __init__(self,data):
                self.data=data
                self.nextnode=None


class LinkedList:
        def __init__(self):
                self.head=None

        def Insert_at_beganing(self,data):
                self.data=data

                newnode=Node(data)

                newnode.nextnode=self.head
                self.head=newnode
        def Insert_at_end(self,data):
                self.data=data
                new_node=Node(data)
                
                temp=self.head
                
                if temp is None:
                        temp=new_node
                        return 
                while (temp.nextnode):
                        temp=temp.nextnode
                temp.nextnode=new_node

        def remove_from_beganing(self):
                if self.head is None:
                        return
                if self.head is not None:
                        self.head=self.head.nextnode


        def remove_data(self,data1):
                ptr=self.head
                if self.head is None:
                        return
                while self.head.nextnode.data==data1:
                        ptr=self.head
                        self.head=self.head.nextnode
                        self.head=self.head.nextnode

                ptr.nextnode=self.head

 
                

        def printfun(self):

                ptr=self.head
                while ptr!=None:
                        print(ptr.data,end=' ')
                        ptr=ptr.nextnode
                        
                
                
if __name__=="__main__":
        list1=LinkedList()
        for i in range(3):
                num=int(input("enter the number :"))
                list1.Insert_at_beganing(num)
        for j in range(4):
                num1=int(input("enter the input at the end:"))
                list1.Insert_at_end(num1)
        print("the list is :")
        list1.printfun()
        list1.remove_data(8)
        list1.remove_from_beganing()
        print('the list after deletion')
        list1.printfun()
        

                                
