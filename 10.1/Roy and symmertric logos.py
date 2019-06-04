t=int(input())
for _ in range(t):
        l=[]
        n=int(input())
        for i in range(n):
                l.append([])
                k=input()
                for j in k:
                        l[i].append(int(j))

        for i in range(n):
                min=0
                max=n-1
                logo=True
                while min<=max:
                        if l[i][min]!=l[i][max] or l[min][i]!=l[max][i]:
                                logo=False
                                break
                        min+=1
                        max-=1
                if logo==False:
                        break
        if logo==False:
                print('NO')
        else:
                print('YES')
                        
