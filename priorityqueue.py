import math

class MinPriorityQueue():
    def __init__(self, max_size) -> None:
        self.max_size = max_size
        self.size = 0
        self.heap = [math.inf] * (max_size + 1) # sum one because the 0 index is not used

    def __len__(self):
        return self.size
    
    def __bool__(self):
        return len(self) > 0
    
    def push(self, value):
        self.size += 1
        self.heap[self.size] = value
        self._swim(self.size)

    def _swim(self, index):
        while index > 1 and self._less(index, index // 2):
            parent_index = index // 2
            self._swap(index, parent_index)
            index = parent_index
 
    def pop(self):
        if not self.size:
            return None
        min = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap[self.size] = math.inf
        self.size -= 1
        self._sink(1)
        return min

    def _sink(self, index):
        while index * 2 <= self.size:
            child_index = index * 2
            # check which child has the smallest value
            if child_index < self.size and self._less(child_index + 1, child_index): 
                child_index += 1

            # if the parent is smaller than both childs, the heapify is done
            if self._less(index, child_index):
                break
            
            self._swap(index, child_index)
            index = child_index

    def _less(self, i, j):
        return self.heap[i] < self.heap[j]
    
    def _swap(self, i, j):
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp

    
