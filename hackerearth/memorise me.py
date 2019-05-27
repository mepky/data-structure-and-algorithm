from collections import Counter
n=int(input())
l=list(map(int,input().split(' ')))
q=int(input())
p=Counter(l)
for _ in range(q):
        x=int(input())
        if p[x]:
                print(p[x])
        else:
                print('NOT PRESENT')
                
        
       
        
