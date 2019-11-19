a=list(map(int,input().split()))


n=len(a)
def findmin(a):
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if mid>0 and a[mid-1]>a[mid]:
            return a[mid]
        if mid<n-1 and a[mid]>a[mid+1]:
            return a[mid+1]

        if a[mid]>a[n-1]:
            low=mid+1
        else:
            high=mid-1
    

print(findmin(a))
