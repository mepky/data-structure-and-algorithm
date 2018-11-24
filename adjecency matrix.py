import numpy as np
n=int(input('number of vertices:'))
e=int(input('number of edge:'))
m=max(n,e)
mat=np.zeros((n,n))
def adj_mat(n,e):
        for i in range(n):
                nec=input().split(' ')
                n=int(nec[0])
                e=int(nec[1])
                cost=int(nec[2])
                mat[n-1][e-1]=cost
                mat[e-1][n-1]=cost
        return mat
print(adj_mat(n,e))
#print(mat)
        
        
