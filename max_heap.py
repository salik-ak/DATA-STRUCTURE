class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 0 and self.heap[i] > self.heap[self.parent(i)]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def extract_max(self):
        if not self.heap:
            return None
        self.swap(0, len(self.heap) - 1)
        max_val = self.heap.pop()
        i = 0
        while self.left(i) < len(self.heap):
            j = self.left(i)
            if self.right(i) < len(self.heap) and self.heap[self.right(i)] > self.heap[j]:
                j = self.right(i)
            if self.heap[j] > self.heap[i]:
                self.swap(i, j)
                i = j
            else:
                break
        return max_val
root=MaxHeap()
root.insert(12)
root.insert(10)
root.insert(15)
root.insert(18)
root.insert(11)
print(root)
print(root.extract_max())    

