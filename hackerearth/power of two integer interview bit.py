class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, A):
        if A==1:
            return 1
        for i in range(2,int(A**0.5)+1):
            p=A
            while p%i==0:
                p=p//i
            if p==1:
                return 1
        else:
            return 0
