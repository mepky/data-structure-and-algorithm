#DP solution for longest increasing subsequence
def lis(p):
	k=len(p)
	l=[1]*(k)
	
	for i in range(1,k):
		for j in range(i):
			if p[i]>p[j] and l[i]<l[j]+1:
				l[i]=l[j]+1

	maximum=0
	for i in range(k):
		maximum=max(maximum,l[i])


	return maximum

arr = [10, 22, 9, 33, 21, 50, 41, 60] 
print("Length of lis is", lis(arr) )


#Recursive solution for lis
def lis(p):
	k=len(p)

	

