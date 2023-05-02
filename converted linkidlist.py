from array import  *

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
arr = array ('i',[1,2,3,4,4,45,6])


def array_to_linked_list(arr):
    head = Node(arr[0])
    prev_node = head

    for i in range(1, len(arr)):
        new_node = Node(arr[i])
        prev_node.next = new_node
        prev_node = new_node

    return head
