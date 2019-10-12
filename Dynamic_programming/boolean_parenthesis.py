def countparenthesis(symb,oper):
	n=len(symb)
	f=[[0]*(n+1) for _ in range(n+1)]
	t=[[0]*(n+1) for _ in range(n+1)]

	#Fill the diagonal element 
	#of f[i][i] and t[i][i]

    # Fill diaginal entries first  
    # All diagonal entries in  
    # T[i][i] are 1 if symbol[i]  
    # is T (true). Similarly, all 
    # F[i][i] entries are 1 if  
    # symbol[i] is F (False)
	for i in range(n):
		if symb[i]=='F':
			f[i][i]=1
		else:
			f[i][i]=0

		if symb[i]=='T':
			t[i][i]=1
		else:
			t[i][i]=0

	for gap in range(1,n):
		i=0
		for j in range(gap,n):
			t[i][j]=f[i][j]=0
			for g in range(gap):
				#find place of paranthesis 
				#using current value of gap
				k=i+g

				#store total[i][k] and total[k+1][j]
				tik=t[i][k]+f[i][k]
				tkj=t[k+1][j]+f[k+1][j]

				if oper[k]=='&':
					t[i][j]+=t[i][k]*t[k+1][j]
					f[i][j]+=(tik*tkj-t[i][k]*t[k+1][j])
				if oper[k]=='|':
					f[i][j]+=f[i][k]*f[k+1][j]
					t[i][j]+=(tik*tkj-f[i][k]*f[k+1][j])
				if oper[k]=='^':
					t[i][j]+=(f[i][k]*t[k+1][j]+t[i][k]*f[k+1][j])
					f[i][j]+=(t[i][k]*t[k+1][j]+f[i][k]*f[k+1][j])
			i+=1

	return t[0][n-1]



symbols = "TTFT"
operators = "|&^"
n = len(symbols) 
  
# There are 4 ways  
# ((T|T)&(F^T)), (T|(T&(F^T))),  
# (((T|T)&F)^T) and (T|((T&F)^T))  
print(countparenthesis(symbols, operators)) 


