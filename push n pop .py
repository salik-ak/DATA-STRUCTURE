class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def display(self):
        for item in reversed(self.items):
            print(item)

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

stack.display()  # output: 30 20 10

stack.pop()
stack.display()  # output: 20 10
