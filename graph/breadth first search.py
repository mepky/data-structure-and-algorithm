class Node(object):
        def __init__(self,name):
                self.name=name
                self.adjacencylist=[]
                self.visited=False
                #self.predecessor=None
class Breadthfirstsearch(object): #BFS we use queue as a adt
        def bfs(self,startnode):
                queue=[]
                queue.append(startnode)
                self.visited=True

                while queue:
                        actualnode=queue.pop(0)
                        print(actualnode.name)
                        for n in actualnode.adjacencylist:
                                if not n.visited:
                                        n.visited=True
                                        queue.append(n)


node1=Node('a')
node2=Node('b')
node3=Node('c')
node4=Node('e')
node5=Node('d')

node1.adjacencylist.append(node3)
node1.adjacencylist.append(node2)
node2.adjacencylist.append(node4)
node4.adjacencylist.append(node5)

bfs=Breadthfirstsearch()
bfs.bfs(node1)
#Comlexity o(v+E) when we use adjacency list 
                
        
