from collections import defaultdict

class Graph:
	def __init__(self,vertices):
		self.v=vertices
		self.graph=defaultdict(list)

	def addEdge(self,u,v):
		self.graph[u].append(v)

class Subset:
	def __init__(self,parent,rank):
		self.parent=parent
		self.rank=rank

#A utility fucntion to find the set of an element 
#node (uses path compression technique)

def find(subsets,node):
	if subsets[node].parent!=node:
		subsets[node].parent=find(subsets,subsets[node].parent)
	return subsets[node].parent
# A function that does union of two sets 
#of u and v (uses union by rank)
def union(subsets,u,v):
	#Attacg smaller rank tree under root
	#if gug rank tree(Uniob by rank)

	if subsets[u].rank>subsets[v].rank:
		subsets[v].parent=u
	elif subsets[v].rank>subsets[u].rank:
		subsets[u].parent=v
	else:
		subsets[v].parent=u
		subsets[u].rank+=1

def isCycle(graph):
	subsets=[]
	for u in range(self.v):
		subsets.append(Subset(u,0))



		for u in self.graph:
			u_rep=find(subsets,u)

			for v in self.graph[u]:
				v_rep=find(subsets,v)

				if u_rep==v_rep:
					return True

				else:
					union(subsets,u_rep,v_rep)



g=Graph(3)
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(0,2)

if isCycle(g):
	print('Graph contains cycle')
else:
	print('Graph does not contains cycle')
