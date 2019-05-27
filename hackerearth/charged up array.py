t=int(input())
for _ in range(t):
        n=int(input())
        l=list(map(int,input().split()))
        sum=0
        d=2**(n-1)
        mod=10**+7
        for i in range(len(l)):
                if d<l[i]:
                        sum+=l[i]
                        sum%=mod
        print(sum)
                        
                        
