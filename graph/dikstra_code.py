#Praveen kumar
#Indian institute of information technology kalyani west bengal
import sys
#v=int(input('enter the vertex:'))
#e=int(input('enter the edge:'))

class Graph:
        def __init__(self,no_of_vertices):
                self.n=no_of_vertices
                self.graph=[0 for row in range(no_of_vertices) for column in range(no_of_vertices)]
        def printsolution(self,dist):
                print('vertex tdistance from source:')
                for v in range(self.n):
                        print('node->',v," ",'distance->',dist[v])



        def min_distance(self,dist,visited):
                min=sys.maxsize

                for i in range(self.n):
                        if dist[i]<min and visited[i]==False:
                                min=dist[i]
                                min_index=i
                return min_index
        
        def dikstra(self,src):
                dist=[sys.maxsize]*self.n
                visited=[False]*self.n
                dist[src]=0
                for cout in range(self.n):
                        u=self.min_distance(dist,visited)

                        visited[u]=True
                        for v in range(self.n):
                                if self.graph[u][v]>0 and visited[v]==False and dist[v]>dist[u]+self.graph[u][v]:
                                        dist[v]=dist[u]+self.graph[u][v]

                self.printsolution(dist)
        

        
g=Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
           [4, 0, 8, 0, 0, 0, 0, 11, 0], 
           [0, 8, 0, 7, 0, 4, 0, 0, 2], 
           [0, 0, 7, 0, 9, 14, 0, 0, 0], 
           [0, 0, 0, 9, 0, 10, 0, 0, 0], 
           [0, 0, 4, 14, 10, 0, 2, 0, 0], 
           [0, 0, 0, 0, 0, 2, 0, 1, 6], 
           [8, 11, 0, 0, 0, 0, 1, 0, 7], 
           [0, 0, 2, 0, 0, 0, 6, 7, 0] 
          ]; 
  
g.dikstra(0); 
  


        
                        
                
                
