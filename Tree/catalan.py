/*Generate a catalan number using Dynamic programming
 o(n**2)
 */

def catalan(n):
	if n==0 or n==1:
		return 1

	val=[0]*(n+1)
	val[0]=val[1]=1
	for i in range(2,n+1):
		val[i]=0
		for j in range(i):
			val[i]=val[i]+val[j]*val[i-j-1]
	return val


for i in range(10):
	print(catalan(i))