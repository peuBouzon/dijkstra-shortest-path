import math

class MinIndexPriorityQueue:
    class QueueFull(Exception):
        pass
    class QueueEmpty(Exception):
        pass

    def __init__(self, max_size) -> None:
        if max_size < 1:
            raise ValueError('The max size should be greater than 0')

        self.max_size = max_size
        self.size = 0
        self.elements = [math.inf] * (max_size + 1) # sum one because the 0 index is not used
        # heap with indexes of self.elements
        self.heap = [None] * (max_size + 1) 
        # maps the index of an element in the heap.
        self.inverse_heap = [-1] * (max_size + 1) # heap[inverse_heap[element]] = element

    def __len__(self):
        return self.size
    
    def __bool__(self):
        return self.size > 0
    
    def contains(self, element):
        return self.inverse_heap[element] != -1

    # Push element at the bottom and "swim" upwards
    def insert(self, index, element):
        if self.size >= self.max_size:
            raise MinIndexPriorityQueue.QueueFull
        self.size += 1
        self.heap[self.size] = index
        self.inverse_heap[index] = self.size
        self.elements[index] = element
        self._swim(self.size)

    # Bottom-up heapify
    def _swim(self, index):
        while index > 1 and self._less(index, index // 2):
            parent_index = index // 2
            self._swap(index, parent_index)
            index = parent_index
    
    def pop(self):
        if self.size <= 0:
            raise MinIndexPriorityQueue.QueueEmpty()
        index_min = self.heap[1]
        min = self.elements[index_min]
        self._swap(1, self.size)
        self.size -= 1
        self._sink(1)
        self.elements[self.heap[self.size + 1]] = None
        self.inverse_heap[self.heap[self.size + 1]] = -1
        return index_min, min

    # Top-down heapify
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

    def change(self, index, element):
        self.elements[index] = element
        self._sink(self.inverse_heap[index])
        self._swim(self.inverse_heap[index])

    def _less(self, i, j):
        return self.elements[self.heap[i]] < self.elements[self.heap[j]]
    
    def _swap(self, i, j):
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp
        self.inverse_heap[self.heap[i]] = i
        self.inverse_heap[self.heap[j]] = j

    
