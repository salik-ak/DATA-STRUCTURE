class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild =None

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
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=BST(data)
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key,end='-->')
        if self.rchild:
            self.rchild.inorder()
    

            

root = BST(10)

list1 = [12,32,43,32,12]
for i in list1:
    print(root.insert(i))

root.inorder()