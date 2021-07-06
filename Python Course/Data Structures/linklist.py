class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None

    def in_front(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next :
                temp=temp.next
            temp.next=new_node
            
    def after_given(self,position,data):
        new_node=Node(data)
        if position==0:
            new_node.next=self.head
            self.head=new_node
            return
        temp=self.head
        l=0
        while(temp):
            if l<position:
                prev=temp
                temp=temp.next
                l+=1
            else:
                break
        prev.next=new_node
        new_node.next=temp

    def delete(self,data):
        if self.head==None:
            return
        temp=self.head
        if temp.data==data:
            self.head=temp.next
            return
        while(temp):
            if temp.data==data:
                break
            
            prev=temp
            temp=temp.next
        prev.next=temp.next

    def traverse(self):
        temp=self.head
        while(temp):
            print(temp.data,id(temp))
            temp=temp.next
    
#creating object for linkedList class
llist=LinkedList()

#creating nodes
first=Node(1)
second=Node(2)
third=Node(3)

#linking nodes with each other
llist.head=first
first.next=second
second.next=third

llist.in_front(5)
llist.at_end(6)
llist.after_given(0,10)
llist.after_given(6,9)
llist.traverse()
llist.delete(5)
print('-'*50)
llist.traverse()
