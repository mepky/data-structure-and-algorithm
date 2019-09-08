from collections import defaultdict

class Graph:
	def __init__(self,vertices):
		self.v=vertices
		self.graph=defaultdict(list)

	def addEdgge(self,u,v):
		self.graph[u].append(v)
	# utility function to find the Subset of element i
	def find_parent(self,parent,i):
		if parent[i]==-1:
			return i
		if parent[i]!=-1:
			self.find_parent(parent,parent[i])

	#Utility function to do union with two subset
	def union(self,parent,x,y):
		x_set=self.find_parent(parent,x)
		y_set=self.find_parent(parent,y)
		parent[x_set]=y_set

	#The main function to check weather a given
	#graph contains cycle or not

	def isCyclic(self):
		parent=[-1]*(self.v)
		#Iterate through all edges of graph ,find subset of both
		#vertices of every edge ,if both subset are same them 
		#There is cycle in graph


		for i in self.graph:
			for j in self.graph[i]:
				x=self.find_parent(parent,i)
				y=self.find_parent(parent,j)
				if x==y:
					return True

				self.union(parent,x,y)


g=Graph(3)
g.addEdgge(0,1)
g.addEdgge(1,2)
g.addEdgge(2,0)

if g.isCyclic():
	print('Graph contains cycle')
else:
	print('Graph does not contain cycle')