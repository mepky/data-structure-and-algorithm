class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        SUM=0
        while A>0:
            SUM+=A//5
            A=A//5
        return SUM
