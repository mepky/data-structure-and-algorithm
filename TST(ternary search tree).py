class Node:
        def __init__(self,charachter):
                self.charachter=charachter
                self.leftnode=None
                self.rightnode=None
                self.middlenode=None
                self.value=0

class TST:
        def __init__(self):
                self.rootnode=None
        def put(self,key,values):
                self.rootnode=self.putitem(self.rootnode,key,values,0)
        #insert values
        def putitem(self,node,key,values,index):
                c=key[index]
                if node==None:
                        node=Node(c)
                if c<node.charachter:
                        node.leftnode=self.putitem(node.leftnode,key,values,index)
                elif c>node.charachter:
                        node.rightnode=self.putitem(node.rightnode,key,values,index)
                elif index<len(key)-1:
                        node.middlenode=self.putitem(node.middlenode,key,values,index+1)
                else:
                        node.value=values
                return node
        def get(self,key):
                node=self.getitem(self.rootnode,key,0)
                if node==None:
                        return -1
                return node.value
        #getting values of key
        def getitem(self,node,key,index):
                if node==None:
                        return None
                c=key[index]
        #TST traversing for getting values at given key
                if c<node.charachter:
                        return self.getitem(node.leftnode,key,index)
                elif c>node.charachter:
                        return self.getitem(node.rightnode,key,index)
                elif index<len(key)-1:
                        return self.getitem(node.middlenode,key,index+1)
                else:
                        return node



if __name__=="__main__":
        t=TST()
        t.put('praveen',3)
        t.put('deepak',4)
        t.put("csk",5)
        t.put("srh",6)
        print(t.get('praveen'))
        
        

















                
                
