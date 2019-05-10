n=int(input())
l=list(map(int,input().split()))
m=list(map(int,input().split()))

k=0
t=0
while(k!=n):
        if (l[0]==m[0]):
                t+=1
                x=l.pop(0)
                y=m.pop(0)
                k+=1

        else:
                x=l.pop(0)
                l.append(x)
                t+=1

print(t)
        
