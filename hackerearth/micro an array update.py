t=int(input())
for _ in range(t):
        n,k=map(int,input().split())
        l=list(map(int,input().split()))
        m=min(l)
        if k-m>0:
                print(k-m)
        else:
                print('0')
