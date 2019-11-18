t=int(input())
for _ in range(t):
    n,k=list(map(int,input().split()))
    l=list(map(int,input().split()))
    s=0
    flag=0
    for i in range(n):
        s+=l[i]-k
        if s<0:
            print('NO',i+1)
            break
    if flag==0:
        print('YES')
        
    
    
