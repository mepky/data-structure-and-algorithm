#from collections import Counter
n=int(input())
l=list(map(int,input().split(' ')))
q=int(input())
#p=Counter(l)

l1=[0]*1001
for i in l:
        l1[i]=l1[i]+1
for _ in range(q):
        x=int(input())
        if l1[x]!=0:
                print(l1[x])
        else:
                print('NOT PRESENT')
        

