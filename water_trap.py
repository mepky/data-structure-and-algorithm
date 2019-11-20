l=list(map(int,input().split()))

stack=[]
water=0
def trap(l):
    for i in l:
        if stack and stack[0]<=i:
            h=stack[0]
            while stack:
                n=stack.pop()
                water+=(h-n)

        stack.append(i)

    h=stack.pop()
    while stack:
        n=stack.pop()
        if n>h:
            h=n
            continue
        water+=h-n

    return water


print(trap(l))
