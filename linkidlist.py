from array import  *
import numpy as np
import math
array1 = array ('i',[1,2,3,4,4,45,6])





print(array1.buffer_info())

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None 


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(head):
    prime_head = None
    prime_tail = None
    node = head
    while node is not None:
        if is_prime(node.value):
            new_node = Node(node.value)
            if prime_head is None:
                prime_head = new_node
                prime_tail = new_node
            else:
                prime_tail.next = new_node
                prime_tail = new_node
        node = node.next
    return prime_head





twoDarray = np.array([[2,3,4],[3,4,1],[9,8,7]])
print(twoDarray)

p=np.append(twoDarray,[[6,7,4]],axis=1)

print(p)

