Python 3.6.8 (default, Oct  7 2019, 12:59:55) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
def largestRectangle(h):
    stack=[]
    result=0
    i=0
    while i<len(h):
        if not stack or h[stack[-1]]<=h[i]:
            stack.append(i)
            i+=1
        else:
            p=stack.pop()
            ans=h[p]*(i-stack[-1]-1 if stack else i)
            if result<ans:
                result=ans
    while stack:
        p=stack.pop()
        ans=h[p]*(i-stack[-1]-1 if stack else i)
        if ans>result:
            result=ans

    return result



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
