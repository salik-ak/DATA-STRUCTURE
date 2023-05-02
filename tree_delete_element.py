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
                return f'added to left side{data}'
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)
                return f'added to right side{data}'
    def search(self,data):
        if self.key == data:
            print("node is found")
            return
        if data <self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("node is not found in tree")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("node is not present in tree")

    def preorder(self):
        print(self.key,end='-->')
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key,end='-->')
        if self.rchild:
            self.rchild.inorder()
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key,end='-->')

root = BST(10)
print(root.key)
print(root.insert(12))
print(root.insert(9))
print()
root.preorder()
print()
root.inorder()
print()
root.postorder()
print()
root.search(122)


        
