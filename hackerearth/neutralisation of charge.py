n=int(input())
s=input()
l=list(s)

stack=[]
for i in range(len(l)):
        stack.append(l[i])
        try:
                if stack[-1] and stack[-2]:
                        if stack[-1]==stack[-2]:
                                stack.pop()
                                stack.pop()

        except:
                pass
print(len(stack))


print(''.join(stack))
