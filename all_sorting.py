def selection_sort(a):
	l=len(a)
	for i in range(l):
		min_i=i
		for k in range(i+1,l):
			if a[min_i]>a[k]:
				min_i=k

		a[i],a[min_i]=a[min_i],a[i]
		
	return a

def bubble_sort(a):
	n=len(a)
	for j in range(len(a)-1):
		for i in range(n-j-1):
			if a[i]>a[i+1]:
				a[i+1],a[i]=a[i],a[i+1]

	return a

def insertion_sort(a):
	n=len(a)
	for i in range(n):
		j=i-1
		key=a[i]
		while j<i and j>=0 and a[j]>key:
			a[j+1]=a[j]
			j=j-1
		a[j+1]=key

	return a


def quick_sort(a,low,high):
	if low<high:
		pivot=findpivot(a,low,high)

		quick_sort(a,low,pivot-1)
		quick_sort(a,pivot+1,high)
	return a

def findpivot(a,low,high):
	pivot=a[high]
	i=low-1
	for j in range(low,high):
		if a[j]<=pivot:
			i+=1
		a[i],a[j]=a[j],a[i]
	a[i+1],a[high]=a[high],a[i+1]

	return (i+1)

def merge_sort(a,low,high):
	if low<high:
		mid=(low+high)//2

		merge_sort(a,low,mid)
		merge_sort(a,mid+1,high)
		merge(a,low,mid,high)
	return a

def merge(a,l,m,h):
	
	n1=(m-l+1)
	l1=[0]*n1
	n2=(h-m)
	l2=[0]*n2
	for i in range(n1):
		l1[i]=a[l+i]
	for j in range(n2):
		l2[j]=a[m+j+1]

	i=0
	j=0
	k=0
	while i<n1 and j<n2:
		if l1[i]>l2[j]:
			a[k]=l2[j]
			k+=1
			j+=1
		else:
			a[k]=l1[i]
			i+=1
			k+=1

	while i<n1:
		a[k]=l1[i]
		i+=1
		k+=1
	while j<n2:
		a[k]=l2[j]
		j+=1
		k+=1













a=[2,4,1,3]
print('selection_sort:')
print(selection_sort(a))
print('Bubble_sort :')
print(bubble_sort(a))
print('Insertion sort')
print(insertion_sort(a))
print('quick_sort :')
print(quick_sort(a,0,len(a)-1))
print('Merge sort:')
print(merge_sort(a,0,len(a)-1))
