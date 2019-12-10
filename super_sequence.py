#Dynamic programming for super sequence

def supersequence(a,b):
	m=len(a)
	n=len(b)

	l=lcs(a,b)
	return (m+n-l)

def lcs(a,b):
	m=len(a)
	n=len(b)

	val=[[0]*(n+2) for _ in range(m+2)]

	for i in range(1,m+1):
		for j in range(n+1):

			if i==0 or j==0:
				val[i][j]=0
			elif a[i-1]==b[j-1]:
				val[i][j]=val[i-1][j-1]+1
			else:
				val[i][j]=max(val[i-1][j],val[i][j-1])

	return val[m][n]

# Driver code 
X = "AGGTAB"
Y = "GXTXAYB"
  
print("Length of the shortest supersequence is %d"
                      % supersequence(X, Y))