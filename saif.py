from collections import defaultdict
x=int(input())
l=defaultdict(int)
k=list()
k.append(1)
l[1]=1
for i in range(x):
    if l[k[-1]]>1:
        k.append(k[-1]+2)
        l[k[-1]]+=1
    else:
        k.append(1)
        l[k[-1]]+=1

print(l[k[x-1]])
