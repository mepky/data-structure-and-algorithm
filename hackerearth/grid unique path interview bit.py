class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        L=1
        for I in range(B,A+B-1):
            L*=I
            L/=(I-B+1)
        return int(L)
            
            
