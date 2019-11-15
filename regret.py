def smallest(arr):
    stack=list()
    stack.append(arr[0])
    print(arr[0],'-----',-1)
    for i in range(1,len(arr)):
        if arr[i]>stack[-1]:
            print(arr[i],'-----',stack[-1])
            stack.append(arr[i])
        else:
            while len(stack)>0:
                p=stack.pop()
                if p<arr[i]:
                    print(arr[i],'------',p)
                    break
            else:
                print(arr[i],'-----',-1)
            stack.append(arr[i])

arr=list(map(int,input().split()))
smallest(arr)
