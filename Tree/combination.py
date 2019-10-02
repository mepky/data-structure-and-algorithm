def combination(n,k):
	if k>n-k:
		k=n-k
	res=1

	for i in range(k):
		res=res*(n-i)
		res=res/(i+1)
	return res

print(combination(6,2))
print(combination(6,4))
l=combination(18,9)
print(l//10)
