class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.head=None

    def insert(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp:
            if new_node.data<temp.data:
                prev=temp
                temp=temp.left
            else:
                prev=temp
                temp=temp.right
        if new_node.data<prev.data:
            prev.left=new_node
            
        else:
            prev.right=new_node
            
    def inOrder(self,root):
        if root:
            self.inOrder(root.left)
            print(root.data,end=' ')
            self.inOrder(root.right)

    def preOrder(self,root):
        if root:
            print(root.data,end=' ')
            self.preOrder(root.left)
            self.preOrder(root.right)

    def postOrder(self,root):
        if root:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.data,end=' ')


# preorder Root left right
# Inorder Left Root right
# Postorder Left Right Root


tree=Tree()
tree.insert(4)
tree.insert(2)
tree.insert(3)
tree.insert(1)
tree.insert(5)
tree.insert(6)

print('Inorder traversal is')
tree.inOrder(tree.head)
print('\nPreorder traversal is')
tree.preOrder(tree.head)
print('\nPostorder traversal is')
tree.postOrder(tree.head)

        
            
