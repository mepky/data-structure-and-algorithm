def greater(arr):
    stack=list()
    stack.append(arr[0])
    for i in range(1,len(arr)):
        while len(stack)>0 and arr[i]>stack[-1]:
            print(stack[-1],'-----',arr[i])
            stack.pop()
        
        stack.append(arr[i])
            
        #stack.append(arr[i])
    while len(stack)>0:
        print(stack.pop(),'-----',-1)

arr=list(map(int,input().split()))
greater(arr)
