class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        sum=0
        n=len(A)
        for i in range(n):
            sum=sum*26
            sum+=ord(A[i])-64
            
        
        return sum
            
