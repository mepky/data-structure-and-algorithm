
a,n,d=map(int,input().split())
def power(a,n,d):
    res=1
    while n>0:
        if n&1>0:
            res=(res*a)%d
        a=a**2%d
        n=n//2
    return res
    
print(power(a,n,d))
