class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None

    def create(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        return self.head
    def append(self,data):
        new_node=Node(data)
        last=self.head
        if self.head is None:
            self.head=new_node
            return 
        while last.next :
            last=last.next
       
        last.next=new_node
        return last.next
       
        
    def printlist(self):
        while self.head  is not None:
            print(self.head.data)
            self.head=self.head.next

    def p(self):
        temp=self.head
        return temp

    def palindrome(self,A):
        head=A
        l=0
        while head is not None:
            head=head.next
            l+=1
        prev=None
        cur=A
        for i in range(l//2):
            nex=cur.next
            cur.next=prev
            prev=cur
            cur=nex
            
            
        if l%2==1:
            cur=cur.next
        for i in range(l//2):
            if prev.data!=cur.data:
                return 'Not palindrome'
            prev=prev.next
            cur=cur.next
        return 'Palindrome'
    def removed_duplicate(self,A):
        temp=A.next
        head=A
        cur=A
        while cur:
            while cur.next:
                if temp.data==cur.data:
                    temp=temp.next
                else:
            
                    cur.next=temp
                cur=cur.next
        return head
l=linkedlist()

for i in range(1,10):
    l.create(i)
    if i==5:
        l.create(5)

k=l.p()
l.removed_duplicate(k)
l.printlist()
#print(l.palindrome(k))

        
    
            
        
