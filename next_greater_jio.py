a=list(map(int,input().split(' ')))

def next_greater(a):
    l=list()
    l.append(a[0])
    k=list()
    for i in range(1,len(a),1):
        val=a[i]
        if len(l)>0:
            ele=l.pop()
            while ele<val:
                #print(str(ele)+'-----'+str(val))
                k.append(val)
                if len(l)==0:
                    break
                ele=l.pop()
            if ele>val:
                l.append(ele)

        l.append(val)

    while len(l)>0:
        ele=l.pop()
        val=-1
        k.append(val)
        #print(str(ele)+'------'+str(val))
    return k
        
            
print(next_greater(a))

        
                
            
            
