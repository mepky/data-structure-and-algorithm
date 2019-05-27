import math
class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        # S=1
        # while A>0:
        #     S+=1
        #     A=A//10
        if A<0:
            return 0
        if A==0:
            return 1
        S=int(math.log10(A)+1)
        
        while A>0:
            last_digit=A%10
            first_digit=A//(10**(S-1))
            if last_digit!=first_digit:
                return 0
            else:
                
                A=A%(10**(S-1))
                A=A//10
                S=S-2
        return 1
                
