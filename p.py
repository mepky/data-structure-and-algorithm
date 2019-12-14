t=int(input())
for _ in range(t):

    n=int(input())
    l=[0]*12
    for _ in range(n):

        k,p=map(int,input().split(' '))
        l[k]=max(l[k],p)

    print(sum(l[:9]))

    
    
