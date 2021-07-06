class Queue:
    def __init__(self):
        self.queue=[]

    def push(self,data):
        self.queue.append(data)
        print(str(data)+' push in the queue')

    def isempty(self):
        return self.queue==[]
    
    def remove(self):
        if self.isempty():
            print('queue is empty')
            return
        l=self.queue.pop(0)
        print(str(l)+' removed from queue')
        
    def print_queue(self):
        print(*self.queue)

ob=Queue()
ob.push(3)
ob.push(4)
ob.push(5)
ob.push(6)
ob.remove()
ob.remove()
ob.print_queue()
