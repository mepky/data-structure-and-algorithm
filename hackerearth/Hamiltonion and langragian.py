n=int(input())
l=list(map(int,input().split()))[::-1]
m=l[0]
p=[]
p.append(l[0])
for i in range(1,n):
        if l[i]>=m:
                p.append(l[i])
                m=l[i]
print(*p[::-1])
                
        
