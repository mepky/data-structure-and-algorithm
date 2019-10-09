
'''
#Recursive solution of lcs
def lcs(x,y,m,n):
	if m==0 or n==0:
		return 0

	elif x[m-1]==y[n-1]:
		return 1+lcs(x,y,m-1,n-1)
	else:
		return max(lcs(x,y,m-1,n),lcs(x,y,m,n-1))

'''

# Dynamic programming solution of LCS
 
def lcs(x,y):
	m=len(x)
	n=len(y)

	l=[[None]*(n+1) for i in range(m+1)]

	for i in range(m+1):
		for j in range(n+1):
			if i==0 or j==0:
				l[i][j]=0

			elif x[i-1]==y[j-1]:
				l[i][j]=1+l[i-1][j-1]

			else:
				l[i][j]=max(l[i][j-1],l[i-1][j])


	return l[m][n]




X = "AGGTAB"
Y = "GXTXAYB"
#print( "Length of LCS is ", lcs(X , Y, len(X), len(Y)))
print(lcs(X,Y))