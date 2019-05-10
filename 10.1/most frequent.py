from collections import Counter
n=int(input())
l=list(map(int,input().split()))
d=[0]*10000
'''p=Counter(l)
k=100000
for k,v in l.items():
        if v=max(l.values()):
                x=min(k,x)
print(x)
'''
for i in l:
        d[i]=d[i]+1

g=[]
p=max(d)
for i in range(len(d)):
       
        if d[i]==p:
                g.append(l[i])
        
print(min(g))


