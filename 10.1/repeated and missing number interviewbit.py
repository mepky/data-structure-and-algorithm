from collections import Counter
a=[3,1,2,3,5]
counter=Counter(a)
p=[]

for i,j in counter.items():
        if j==2:
                p.append(i)
                break
for i in range(1,len(a)+1):
        if i  not in counter:
                p.append(i)
print(p)
                
        
