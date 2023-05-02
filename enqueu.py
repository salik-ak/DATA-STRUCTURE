
# class Queue:
#     def __init__(self):
#         self.items = []

#     def enqueue(self, item):
#         self.items.append(item)

#     def dequeue(self):
#         if len(self.items) == 0:
#             return None
#         return self.items.pop(0)

#     def display(self):
#         print(self.items)








# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.display()  # Output: [1, 2, 3]
# q.dequeue()  # Output: 1
# q.display()  # Output: [2, 3]

queue = []

# Adding elements to the queue
queue.append('apple')
queue.append('banana')
queue.append('cherry')

print("Queue:", queue)

# Removing elements from the queue
first_element = queue.pop(0)
second_element = queue.pop(0)

print("First element removed:", first_element)
print("Second element removed:", second_element)
print("Queue after removal:", queue)


