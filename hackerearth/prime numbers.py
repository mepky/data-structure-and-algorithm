def sieve(A):
        l=[True]*(A+1)
        l[0]=l[1]=False
        k=[]
        for i in range(2,int(A**0.5)+1):
            if l[i]==True:
                
                for j in range(2*i,A+1,i):
                    l[j]=False
                    
        for i in range(A+1):
            if l[i]==True:
                k.append(i)
        return k
               
print(sieve(1000000))
