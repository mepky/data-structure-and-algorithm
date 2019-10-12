def optimalstrategy(a):
	n=len(a)
	table=[[0]*n for _ in range(n)]
	

	#Table is filled in diagonal fashion 

	for gap in range(n):
		for j in range(gap,n):
			i=j-gap

			x=0
			if ((i+2)<=j):
				x=table[i+2][j]
			y=0
			if (i+1)<=(j-1):
				y=table[i+1][j-1]
			z=0
			if (i<=j-2):
				z=table[i][j-2]
			table[i][j]=max(a[i]+min(x,y),a[j]+min(y,z))

	return table[0][n-1]

arr1 = [ 8, 15, 3, 7 ] 
n = len(arr1) 
print(optimalstrategy(arr1)) 
  
arr2 = [ 2, 2, 2, 2 ] 
n = len(arr2) 
print(optimalstrategy(arr2)) 
  
arr3 = [ 20, 30, 2, 2, 2, 10] 
n = len(arr3) 
print(optimalstrategy(arr3)) 