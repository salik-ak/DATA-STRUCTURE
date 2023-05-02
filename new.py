
import queue

# def recursion (n):
#     if n == 0:
#         return 1
#     else:
#         return n * recursion(n-1)
    
# f = recursion(6)
# print(

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.ref = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def printLL(self):
#         if self.head is None:
#             print("empty list")
#         else:
#             n =self.head
#             while n is not None:
#                 print (n.data)
#             n= n.ref

#     def add_node(self,data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             n = self.head 
#             while n.ref is not None:
#                 n = n.ref
#         n.ref = new_node

#     def search(self,data):
#         current = self.head

# Create an empty queue
# my_queue = queue.Queue()

# # Enqueue elements to the queue
# my_queue.put('apple')
# my_queue.put('banana')
# my_queue.put('cherry')

# # Print the queue
# print(my_queue.queue)

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)
my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print(my_stack.pop())  # output: 3
print(my_stack.peek())  # output: 2
print(my_stack.size())  # output: 2
print(my_stack.is_empty())  # output: False
