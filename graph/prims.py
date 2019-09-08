import sys

class Graph():
	def __init__(self,vertices):
		self.v=vertices
		self.graph=[[0 for column in range(vertices)] for row in range(vertices)]

#minimum distance vale form the oset of vertices 
	def minval(self,key,mstset):
		min=sys.maxsize
		min_index=0
		for i in range(self.v):
			if key[i]<min and mstset==False:
				min=key[i]
				min_index=i
		return min_index
#Construct and print mst for graph 
	def prims(self):
			#Key values used to pick minimum weight edge in cit 
		key=[sys.maxsize]*self.v
		parent=[None]*self.v
		key[0]=0#AS THIS VERTEX AS PICTKES AS FIRST
		mstset=[False]*self.v
		parent[0]=-1#first node is always the root node

		for cout in range(self.v):
			u=self.minval(key,mstset)
			mstset[u]=True

			for i in range(self.v):
				if self.graph[u][i]>0 and mstset[i]==False and key[i]>self.graph[u][i]:
					key[i]=self.graph[u][i]
					parent[i]=u



		self.printmst(parent)

	def printmst(self,parent):
		print('Edge \tWeight')
		for i in range(1,self.v):
			print(parent[i],'--',i,'\t',self.graph[i][parent[i]])






		





g = Graph(5) 
g.graph = [ [0, 2, 0, 6, 0], 
            [2, 0, 3, 8, 5], 
            [0, 3, 0, 0, 7], 
            [6, 8, 0, 0, 9], 
            [0, 5, 7, 9, 0]] 
  
g.prims(); 
  