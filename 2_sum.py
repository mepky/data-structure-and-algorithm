a=list(map(int,input().split()))
b=int(input())
def t00_sum(a,b):
    p={}

    for i,val in enumerate(a):
        if val in p:
            return p[val]+1,i+1
        if b-val not in p:
            p[b-val]=i

    return []

print(t00_sum(a,b))
