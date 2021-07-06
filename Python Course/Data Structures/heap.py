from heapq import heappush, heappop, heapify 
 
# heappop - pop and return the smallest element from heap,
# maintaining the heap invariant.

# heappush - push the value item onto the heap,
# maintaining heap invarient.

# heapify - transform list into heap, in place,
# in linear time
 
class MinHeap:
    def __init__(self):
        self.heap = []



    def heapify(self,arr):
        heapify(arr)
        self.heap=arr
        return self.heap
 
    def parent(self, i):
        return (i-1)//2
     
    def insertKey(self, k):
        heappush(self.heap, k)
        print(self.heap)
 
    def decreaseKey(self, i, new_val):
        self.heap[i]  = new_val 
        while(i != 0 and self.heap[self.parent(i)] > self.heap[i]):
            self.heap[i] , self.heap[self.parent(i)] = (
            self.heap[self.parent(i)], self.heap[i])
            i=self.parent(i)
             
    def extractMin(self):
        return heappop(self.heap)
 
    def deleteindex(self, i):
        self.decreaseKey(i, float("-inf"))
        self.extractMin()
 
    def getMin(self):
        return self.heap[0]

heapObj = MinHeap()

heapObj.insertKey(3)
heapObj.insertKey(2)
heapObj.insertKey(15)
heapObj.insertKey(5)
heapObj.insertKey(4)
heapObj.deleteindex(3)
heapObj.insertKey(45)
heapObj.insertKey(1)
heapObj.heapify([3,2,15,5,4,45,1])
print(heapObj.heap)
heapObj.insertKey(6)
print(heapObj.heap)
heapObj.deleteindex(3)
print(heapObj.heap)

