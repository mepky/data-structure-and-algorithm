a=list(map(int,input().split()))
b=int(input())
def count_occurence(a,b,first=True):
    low=0
    n=len(a)
    high=n-1
    result=0
    while low<=high:
        mid=(low+high)//2
        if a[mid]==b:
            result=mid
            if first:
                high=mid-1
            else:
                low=mid+1

        elif a[mid]>b:
            high=mid-1
        else:
            low=mid+1
    return result

f=count_occurence(a,b)
c=count_occurence(a,b,False)
if f==-1:
    print('0')
else:
    print(c-f+1)
    



            
            
    
