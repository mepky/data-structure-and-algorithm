t=int(input())

# def findxor(int(a),int(b)):
# 	return ((a|b) - (a & b))

# def find_AND(int(a),int(b)):

# 	return (a&b)


for _ in range(t):

	a=input()
	b=input()
	#a=int(a,2)
	#b=int(b,2)
	# c=a
	# d=b
	#cnt=0
	# def add(a,b):
	# 	cnt=0
	# 	while b>0:
	# 		u=a^b
	# 		v=a & b
	# 		a=u
	# 		b=v*2
	# 		cnt+=1
	# 	return cnt

	# print(add(c,d))
	# a=int(a)
	# b=int(b)
	cnt=0
	while int(b,2)>0:
		u=a^b
		v=a & b
		a=u
		b=str(v)+'0'
		# b=int(b)
		cnt+=1
	print(cnt)



