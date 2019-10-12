def countodd(dist):
	n=len(dist)
	dp=[[0 for i in range(2)] for j in range(n)]

	cnt=[[0 for i in range(2)] for j in range(n)]

	for i in range(n):
		for j in range(2):
			if dist[i][j]%2==0:
				cnt[i][0]+=1
			else:
				cnt[i][1]+=1
	dp[0][0]=cnt[0][0]
	dp[0][1]=cnt[0][1]

	for i in range(1,n):
		dp[i][0]=dp[i-1][0]*cnt[i][0]+dp[i-1][1]*cnt[i][1]
		dp[i][1]=dp[i-1][1]*cnt[i][0]+dp[i-1][0]*cnt[i][1]

	return dp[n-1][1]

a = [[1, 2] , [3, 6] ] 
n = len(a) 
print(countodd(a))