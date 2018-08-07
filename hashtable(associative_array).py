class Hash:
        def __init__(self):
                self.size=10
                self.keys=[None]*self.size
                self.values=[None]*self.size

        def put(self,key,data):
                index=self.hashfunction(key)
                #Here we are dealing with collision case i.e (slot is not empty)
                while self.keys[index] is not None:
                        if self.keys[index]==key:
                                self.values[index]=data
                                return
                        #we are finding next slot which is empty
                        index=(index+1)%self.size
                #insert
                self.keys[index]=key
                self.values[index]=data

        def hashfunction(self,key):
                sum=0
                for pos in range(len(key)):
                        sum=sum+ord(key[pos])
                return sum%self.size
        def get(self,key):
                index=self.hashfunction(key)
                while self.keys[index] is not None:
                        if self.keys[index]==key:
                                return self.values[index]
                        index=index%self.size
                #if hash table is empty
                return None
        #To print the existing vlaue of hashtable
        def phash(self):
                for i in range(self.size):
                        if self.keys[i] is not None:
                                print(self.values[i])
                        
                        
if __name__=="__main__":
        h=Hash()
        h.put('praveen',416)
        h.put('deepak',364)
        h.put('chanchal',284)
        print(h.get('deepak'))
        print('The value inside hash is :')
        h.phash()
                
