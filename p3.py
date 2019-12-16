from collections import defaultdict
t=int(input())
for _ in range(t):
    l=defaultdict(int)
    n=int(input())
    d=2**20
    t=0
    s=input()
    a=[-1]*27
    for i in range(n):
        if a[ord(s[i])-97]==-1:
            a[ord(s[i])-97]=i
        else:

            d=min(d,i-a[ord(s[i])-97])
            t=1
            a[ord(s[i])-97]=i
    if t==0:
        print(0)
    else:
        print(n-d)


            
            
            
            
            
    
