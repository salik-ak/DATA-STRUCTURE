class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
        
    def insert(self,data):
        if self.key is None: 
            self.key = data
            return
        if self.key == data:
            return
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
                return f'item {data} added to left of BST'
            return 'done'
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)
                return f'item {data} added to right of BST'
            return 'added to right'
        
    def preOrder(self):
            print(self.key,end='-->')
            if self.lchild:
                self.lchild.preOrder()
            if self.rchild:
                self.rchild.preOrder()

    def inOrder(self):
            if self.lchild:
                self.lchild.inOrder()
            print(self.key,end='-->')
            if self.rchild:
                self.rchild.inOrder()

    def postOrder(self):
            if self.lchild:
                self.lchild.postOrder()
            
            if self.rchild:
                self.rchild.postOrder()
            print(self.key,end='-->')

root = BST(10)
list1 = [12,43,56,32,2,45]

for i in list1:
    print(root.insert(i))
print(root.insert(23))
print(root.insert(9))
print(root.key)
print(root.lchild)
print(root.rchild.key)
root.preOrder()
print()
root.inOrder()
print()
root.postOrder()




