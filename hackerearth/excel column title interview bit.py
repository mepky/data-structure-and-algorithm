class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        # C=0
        # p=A
        # while p>0:
        #     p=p//26
        #     C+=1
            
        # string=['\0']*(C+1)
        string=[]
        #i=0
        n=A
        while n>0:
            rem=n%26
            
            if rem==0:
                string.append('Z')
                i+=1
                n=n//26-1
            else:
                string.append(chr((rem-1)+ord('A')))
                i+=1
                n=n//26
        #string[i]='\0'
        string=string[::-1]
        return (''.join(string))
