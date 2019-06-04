class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, a):
        
        max1 = -2147483648
        min1 = +2147483647
        max2 = -2147483648
        min2 = +2147483647
        for i in range(len(a)):
            
            max1=max(max1,a[i]+i)
            min1=min(min1,a[i]+i)
            max2=max(max2,a[i]-i)
            min2=min(min2,a[i]-i)
        return max(max1-min1,max2-min2)
            
    
