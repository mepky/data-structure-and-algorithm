#praveen kumar
#Indian institute of information technology kalyani west bengal
import numpy as np
n=int(input('number of vertices:'))
e=int(input('number of edge:'))
m=max(n,e)
mat=np.zeros((n+1,n+1))
def adj_mat(n,e):
        for i in range(1,m+1):
                nec=input().split(' ')
                n=int(nec[0])
                e=int(nec[1])
                #cost=int(nec[2])
                mat[n][e]=1
                mat[e][n]=1
        return mat
print(adj_mat(n,e))
#print(mat)
        
        
