class Stack:
    def __init__(self):
        self.stack=[]

    def push(self,data):
        self.stack.append(data)
        print(str(data)+' push in the stack')

    def is_empty(self):
        return self.stack==[]
    

    def remove(self):
        if self.is_empty():
            print('stack is empty')
            return
        l=self.stack.pop()
        print(str(l)+' removed from stack')
    def print_stack(self):
        print(self.stack)
            
ob=Stack()
ob.push(3)
ob.push(4)
ob.push(5)
ob.push(6)
ob.remove()
ob.remove()
ob.print_stack()
