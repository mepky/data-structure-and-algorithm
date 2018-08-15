class Node(object):
        def __init__(self,name):
                self.name=name
                self.visited=False
                self.adjacencylist=[]
                self.predecessor=None

class Depthfirstsearch(object):
        def dfs(self,node):
                self.visited=True
                print(node.name)

                for n in node.adjacencylist:
                        if not n.visited:
                                self.dfs(n)



node1=Node('a')
node2=Node('1')
node3=Node('ac')
node4=Node('ab')
node5=Node('2')

node1.adjacencylist.append(node2)
node1.adjacencylist.append(node3)
node2.adjacencylist.append(node4)
node4.adjacencylist.append(node5)

dfs=Depthfirstsearch()
dfs.dfs(node1)

