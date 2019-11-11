a=int(input())
a=list(str(a))
a=list(map(int,a))
from collections import defaultdict
def mul(a):
    k=1
    for i  in a:
        k=k*i
    return k
'''
def findcolorful(a):
    p={}

    n=1
    while n<len(a):
        for i in range(len(a)-n+1):
            w=a[i:i+n]
            s=mul(w)

            try:
                p[s]+=1
                return 0
            except:
                p[s]=1
        n+=1
    s=mul(a)
    try:
        p[s]+=1
        return 0
    except:
        pass
    return 1
'''
def findcolorful(a):
    d=defaultdict(int)
    n=1
    while n<len(a):
        for i in range(len(a)-n+1):
            w=a[i:i+n]
            s=mul(w)
            if d[s]>0:
                d[s]+=1
                return 0
            else:
                d[s]=1
        n+=1
    s=mul(a)
    if d[s]>0:
        d[s]+=1
        return 0
    else:
        d[s]=1
    return 1














        

print(findcolorful(a))
    
                
        
