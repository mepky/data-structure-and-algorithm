#Recrusion programm
'''
def subset_sum(a,n,sumt):
	if sumt==0:
		return True 

	if n==0 and sumt>0:
		return False

	if a[n-1]>sumt:
		return	subset_sum(a,n-1,sumt)

	return subset_sum(a,n-1,sumt-a[n-1]) or subset_sum(a,n-1,sumt)

	

set = [3, 34, 4, 12, 5, 2] 
sum = 9

if (subset_sum(set,len(set),sum)==True):
	print('Found a subset  sum')
else:
	print('Subset sum doesnt exists')
'''
#Dynamic programm

def sub_sum(a,sumt):
	n=len(a)
	dp=[[False]*(sumt+1) for i in range(n+1)]
	for i in range(n+1):
		dp[i][0]=True

	for i in range(sumt+1):
		dp[0][i]=False

	for i in range(1,n+1):
		for j in range(1,sumt+1):
			if j<a[i-1]:
				dp[i][j]=dp[i-1][j]
			if j>=a[i-1]:
				dp[i][j]=dp[i-1][j] or dp[i-1][j-a[i-1]]

	return dp[n][sumt]




if __name__=='__main__': 
    set = [3, 34, 4, 12, 5, 2] 
    sum = 9
    n =len(set) 
    if (sub_sum(set,sum) == True): 
        print("Found a subset with given sum") 
    else: 
        print("No subset with given sum") 