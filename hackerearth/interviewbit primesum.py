def primesum(n):
        isprime=[True]*(n+1)
        isprime[0]=isprime[1]=False
        for i in range(2,int(n**0.5)+1):
                if isprime[i]:
                        for j in range(i*2,n+1,i):
                                isprime[j]=False
        print(isprime)

        for i in range(2,n):
                if isprime[i] and isprime[n-i]:
                        return [i,n-i]

        return []

n=int(input())
print(primesum(n))
                        
