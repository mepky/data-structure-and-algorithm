n,q=map(int,input().split())
l=list(map(int,input().split()))
l1=[[None for i in range(3)] for _ in range(q)]
for i in range(q):
        l1[i]=list(map(int,input().split()))

        if l1[i][0]==1:
                if l[l1[i][1]-1]==0:
                        l[l1[i][1]-1]=1
                else:
                        l[l1[i][1]-1]=0
        else:
                if l[l1[i][2]-1]==0:
                        print('EVEN')
                else:
                        print('ODD')
                        
