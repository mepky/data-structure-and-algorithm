class Solution:
	# @param A : integer
	# @return a strings
	def findDigitsInBinary(self, A):
	    l=''
	    if A==0:
	        return '0'
	   
	    while A>0:
	        X=A%2
	        A=A//2
	        l=l+str(X)
	        l1 = ''.join(reversed(l))
	    return l1
