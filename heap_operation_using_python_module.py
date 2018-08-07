from heapq import heappop,heappush,heapify

heap=[]
nums=list(map(int,input("enter the number:").split(' ')))

for num in nums:
        heappush(heap,num)
while heap:
        print(heappop(heap))


heapify(nums) # Here heapify creates min,heap in tree like sturcture

print(nums)
