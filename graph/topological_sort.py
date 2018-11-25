from collections import defaultdict

class Graph:
        def __init__(self,ver):
                self.graph=defaultdict(list)
                self.n=ver
                #ver is number of vertices
        def edge(self,u,v):
                self.graph[u].append(v)
        def topological_sort_utility(self,v,visited,stack):
                visited[v]=True

                for i in self.graph[v]:
                        if visited[i]==False:
                                self.topological_sort_utility(i,visited,stack)

                #push into the stack
                stack.insert(0,v)

        def topological_sort(self):
                visited=[0]*self.n
                stack=[]

                for i in range(self.n):
                        if visited[i]==False:
                                self.topological_sort_utility(i,visited,stack)

                print(stack)

g=Graph(6)
g.edge(5, 2);
g.edge(5, 0); 
g.edge(4, 0); 
g.edge(4, 1); 
g.edge(2, 3); 
g.edge(3, 1);
g.topological_sort()
print('topological sort are:')
                                
                                
                
                
