# Python3 Program to check if array  
# can be split into K contiguous  
# subarrays each having equal sum  
  
# Function returns true to it is possible  
# to create K contiguous partitions each 
# having equal sum, otherwise false  
def KpartitionsPossible(arr, n, k) : 
  
    sum = 0
    count = 0
      
    # calculate the sum of the array  
    for i in range(n) : 
        sum = sum + arr[i] 
      
    if(sum % k != 0) :  
        return 0
      
    sum = sum // k 
    ksum = 0
      
    # ksum denotes the sum of each subarray  
    for i in range(n) :  
        ksum = ksum + arr[i]  
      
    # one subarray is found  
    if(ksum == sum) : 
          
        # to locate another  
        ksum = 0
        count += 1
      
    if(count == k) : 
        return 1
    else : 
        return 0
  
# Driver code  
if __name__ == "__main__" :  
  
    arr = [ 1, 1, 2, 2]  
    k = 2
    n = len(arr) 
    if (KpartitionsPossible(arr, n, k) == 0) : 
        print("Yes") 
    else : 
        print("No")  
  