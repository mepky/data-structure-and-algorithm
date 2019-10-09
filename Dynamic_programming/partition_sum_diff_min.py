'''
#Recursive solution 
def ps(a,i,sumc,sumt):
	if i==0:
		return abs((sumt-sumc)-sumc)

	return min(ps(a,i-1,sumc+a[i-1],sumt),ps(a,i-1,sumc,sumt))

def findmin(a):
	sumt=sum(a)
	return ps(a,len(a),0,sumt)


a = [3, 1, 4, 2, 2, 1] 
print('The minimum difference between two sets is ', findmin(a))

#DP solution of partition problem

'''
import sys
def findmin(a):
	#sum of all the elements
	m=len(a)
	sumt=sum(a)
	#Create an array to store result
	dp=[[0]*(sumt+1) for _ in range(m+1)]
	#Initialize first colums as 1
	for i in range(m+1):
		dp[i][0]=1
	#Initialize top row except dp[0][0] as 0
	for i in range(1,sumt+1):
		dp[0][i]=0
		#Fill the partition table in bottom up manner
	for i in range(1,m+1):
		for j in range(1,sumt+1):
			#If i'th element is excluded
			dp[i][j]=dp[i-1][j]
			#If i'th element is included
			if a[i-1]<=j:
				dp[i][j] |=dp[i-1][j-a[i-1]]

	# Initialize difference of two sums.
	diff=sys.maxsize
	#Find the larges j such that dp[n][j]
	#is 1 where j loops from sum//2 to -1
	for j in range(sumt//2,-1,-1):
		if dp[m][j]==1:
			diff=sumt-2*j
			break

	return diff
#Driver program to test above function
a= [3, 1, 4, 2, 2, 1]
print('Minimum difference between two set is :')
print(findmin(a))