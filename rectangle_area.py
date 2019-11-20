l=list(map(int,input().split()))

def rectangle(l):
    result=0
    stack=list()

    i=0
    while i<len(l):
        if not stack or l[stack[-1]]<=l[i]:
            stack.append(i)
            i+=1
        else:
            p=stack.pop()
            tmp=(l[p]*(i-stack[-1]-1) if stack else i)
            if tmp>result:
                result=tmp

    while stack:
        p=stack.pop()
        tmp=(l[p]*(i-stack[-1]-1) if stack else i)
        if tmp>result:
            result=tmp

    return result

print(rectangle(l))

        

                
