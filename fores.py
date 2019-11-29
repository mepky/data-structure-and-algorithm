t=int(input())
for _ in range(t):
    l=list(map(int,input().split()))
    cnt=0
    for i in range(min(l)+1):
        l.sort(reverse=True)
        if l[2]==0:
            print(cnt+l[1])
        else:
            l[0]-=1
            l[2]-=1
            cnt+=1
        
        
