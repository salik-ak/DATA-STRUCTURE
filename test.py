
# # def factorial(n):
# #     if n == 0:
# #         return 1
# #     else:
# #         return n * factorial(n-1)
    
# # s= factorial(4)
# # print(s)

# class Node:
#     def __init__(self, value=None):
#         self.value = value
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def add_node(self, value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#         else:
#             current_node = self.head
#             while current_node.next is not None:
#                 current_node = current_node.next

#             current_node.next = new_node

#     def print_list(self):
#         current_node = self.head
#         while current_node is not None:
#             print(current_node.value)
#             current_node = current_node.next

#     def print_reverse_list(self, node):
#         if node is None:
#             return
#         self.print_reverse_list(node.next)
#         print(node.value)

# # Example usage
# linked_list = LinkedList()
# linked_list.add_node(1)
# linked_list.add_node(2)
# linked_list.add_node(3)

# print("List in order:")
# linked_list.print_list()

# print("List in reverse order:")
# linked_list.print_reverse_list(linked_list.head)

# Define the node class
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None
class LinkedList:
    def __init__(self):
        self.head = None

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref

            n.ref = new_node
    def linear_search(self, value):
        current = self.head

        while current:
            if current.data == value:
                return True # value found
            current = current.ref

        return False # value not found

list = LinkedList()
list.add_end(23)
list.add_end(25)
list.add_end(28)
list.add_end(39)
print(list.linear_search(5)) # Output: True
print(list.linear_search(25)) # Output: False


        


