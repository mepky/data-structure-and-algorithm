def printcount(dist):
	if dist<0:
		return 0
	if dist==0:
		return 1
	else:
		return (printcount(dist-1)+printcount(dist-2)+printcount(dist-3))



#Dp solution for this proble

def printDp(dist):
	l=[0]*(dist+1)
	l[0]=1
	l[1]=1
	l[2]=2
	l[3]=4

	if dist<0:
		return 0
	for i in range(4,dist+1):
		l[i]=l[i-1]+l[i-2]+l[i-3]

	return l[dist]
dist=6
print('Recursive solution: ')
print(printcount(dist))
print('Dynamic programming solution:')
print(printDp(6))
