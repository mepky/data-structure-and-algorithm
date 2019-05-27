'''
def insertion_sort(a):
        for i in range(1,len(a)):
                l=a[i]

                j=i-1
                while j>=0 and a[j]>l:
                        a[j+1]=a[j]
                        j=j-1
                a[j+1]=l
        return a

a=list(map(int,input().split()))
print(insertion_sort(a))


'''
'''
def merge(arr,start,mid,end):
        temp=[0]*(end-start+1)

        i,j,k=start,mid+1,0

        while i<=mid and j<=end:
                if arr[i]<=arr[j]:
                        temp[k]=arr[i]
                        k+=1
                        i+=1
                else:
                        temp[k]=arr[j]
                        k+=1
                        j+=1

        while i<=mid:
                temp[k]=arr[i]
                k+=1
                i+=1
        while j<=end:
                temp[k]=arr[j]
                k+=1
                j+=1

        for i in range(start,end+1):
                arr[i]=temp[i-start]
        return arr
                


def mergesort(arr,start,end):
        if start<end:
                mid=(start+end)//2
                mergesort(arr,start,mid)
                mergesort(arr,mid+1,end)
                merge(arr,start,mid,end)


arr=list(map(int,input().split()))
print(mergesort(arr,0,len(arr)-1))
for i in range(len(arr)):
        print(arr[i])


'''
def quicksort(array,start,end):
    if start<end:
        pindex=partition(array,start,end)
        quicksort(array,start,pindex-1)
        quicksort(array,pindex+1,end)

def partition(array,start,end):
    pindex=start

    pivot=array[end]
    
    for i in range(start,end):
        if pivot>=array[i]:
            array[i],array[pindex]=array[pindex],array[i]
            pindex +=1
           
    array[end],array[pindex]=array[pindex],array[end]
    return pindex
        

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
quicksort(test,0,len(test)-1)
# for i in range(len(test)):
#     print(test[i])
print(list(test))


















                        
        
