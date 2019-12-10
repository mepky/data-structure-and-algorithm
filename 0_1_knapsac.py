def knapsac(a,w,val):
	n=len(a)
	dp=[[0]*(n+1) for _ in range(w+1)]

	for i in range(n+1):
		for j in range(w+1):
			if i==0 or j==0:
				k[i][j]=0
			elif w[i-1]<=w:
				k[i][j]=max(val[i-1]+k[i-1][w-w[i-1]],k[i-1][w])
			else:
				k[i][w]=k[i-1][w]
		return k[n][w]

	val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
n = len(val) 
print(knapSack(W, wt, val)) 