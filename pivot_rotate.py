a=list(map(int,input().split()))
b=int(input())

def rotated(a):
    low=0
    n=len(a)
    high=n-1
    result=0
    while low<=high:
        mid=(low+high)//2
        if mid>0 and a[mid-1]>a[mid]:
            return mid
        if mid<n-1 and a[mid]>a[mid+1]:
            return mid+1
        if a[mid]>a[n-1]:
            low=mid+1
        else:
            high=mid-1
    


def search(a,b):
    low=0
    n=len(a)
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if a[mid]==b:
            return mid
        elif a[mid]>b:
            high=mid-1
        else:
            low=mid+1

    else:
        return -1
n=len(a)
result=rotated(a)
#print(result)
p=a[0:result]
k=a[result:n]
print('p is:',p)
print('k is ',k)
s=search(p,b)
t=search(k,b)
if s==-1 and t==-1:
    print('NOt fount')
else:
    print(s if s!=-1 else len(p)+t)
    
        


