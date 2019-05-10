n,m=map(int,input().split())
p=[]
k=[[0 for i in range(n)] for j in range(m)]
for i in range(n):
        l=list(map(int,input().split()))
        p.append(l)
def transpose(p, k): 
  
    for i in range(m): 
        for j in range(n): 
            k[i][j] = p[j][i] 

transpose(p,k)
for i in range(m): 
    for j in range(n): 
        print(k[i][j], end=' ') 
    print()   
