class Heap(object):
        HEAP_SIZE=10
        def __init__(self):
                
                self.heap=[0]*Heap.HEAP_SIZE
                self.currentPosition=-1

        def Insert(self,item):
                if self.isFull():
                        print("Heap is full")
                        return
                self.currentPosition=self.currentPosition+1
                self.heap[self.currentPosition]=item
                self.Fixup(self.currentPosition)

        def Fixup(self,index):
                parentindex=int((index-1)/2)

                while parentindex>=0 and self.heap[self.currentPosition]>self.heap[parentindex]:
                        temp=self.heap[self.currentPosition]
                        self.heap[parentindex]=self.heap[self.currentPosition]
                        self.heap[parentindex]=temp
                        

        def isFull(self):
                if self.currentPosition==Heap.HEAP_SIZE:
                        return True
                else:
                        return False

        def Heapsort(self):
                for i in range(0,self.currentPosition+1):
                        temp=self.heap[0]
                        print("%d"%temp)
                        self.heap[0]=self.heap[self.currentPosition-i]
                        self.heap[self.currentPosition-i]=temp
                        self.Fixdown(0,self.currentPosition-i-1)

        def Fixdown(self,index,upto):
                while index<=upto:
                        leftchild=2*index+1
                        rightchild=2*index+2
                        
                        if leftchild<upto:
                                childToswap=None
                                if rightchild>upto:
                                        childToswap=leftchild
                                else:
                                        if self.heap[leftchild]>self.heap[rightchild]:
                                                childToswap=leftchild
                                                
                                        else:
                                                childToswap=rightchild
                                        
                                if self.heap[index]<self.heap[childToswap]:
                                        temp=self.heap[index]
                                        self.heap[index]=self.heap[childToswap]
                                        self.heap[childToswap]=temp

                                else:
                                        break;
                                index=childToswap
                        else:
                                break;
                
                                
                        
                



if __name__=="__main__":
        heap=Heap()
        heap.Insert(41)
        heap.Insert(6)
        heap.Insert(9)
        heap.Insert(111)
        heap.Heapsort()






                        
                
                
