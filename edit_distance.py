
'''def edit(x,y,m,n):
	if m==0:
		return n

	if n==0:
		return m

	if x[m-1]==y[n-1]:
		return edit(x,y,m-1,n-1)
	else:
		return 1+min(edit(x,y,m,n-1),
			edit(x,y,m-1,n),edit(x,y,m-1,n-1))

str1 = "sunday"
str2 = "saturday"
print (edit(str1, str2, len(str1), len(str2))) 
'''
#DP solution for minimun edit distance
def editd(x,y):
	m=len(x)
	n=len(y)
	l=[[0]*(n+1) for i in range(m+1)]

	for i in range(m+1):
		for j in range(n+1):

			if i==0:
				l[i][j]=j
			elif j==0:
				l[i][j]=i
			elif x[i-1]==y[j-1]:
				l[i][j]=l[i-1][j-1]
			else:
				l[i][j]=1+min(l[i-1][j-1],l[i][j-1],l[i-1][j])

	return l[m][n]



str1 = "sunday"
str2 = "saturday"
print (editd(str1, str2)) 














