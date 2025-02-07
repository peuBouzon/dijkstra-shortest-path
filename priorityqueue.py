class PriorityQueue():
    def __init__(self, max_size) -> None:
        self.max_size = max_size
        self.size = 0
        self.heap = [None] * (max_size + 1) # start the index at 1

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.heap[self.size] = value
        self.swim(self.size)

    def swim(self, position):
        parent_position = position // 2
        value_above = self.heap[parent_position]
        current_value = self.heap[position]
        while position > 1 and value_above < current_value:
            self.heap[position] = value_above
            self.heap[parent_position] = current_value
            position = parent_position
 
    def pop(self):
        max = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap[self.size] = None
        self.size -= 1
        self.sink(1)
        return max

    def sink(self, position):
        child_position = position * 2
        while child_position < self.size:

            # check which child has the largest value
            if (self.heap[child_position] < self.heap[child_position + 1]): 
                child_position += 1

            # if the parent is greater than both childs, the heapify is done
            if self.heap[position] > self.heap[child_position]:
                break

            temp = self.heap[position]
            self.heap[position] = self.heap[child_position]
            self.heap[child_position] = temp
            position = child_position


    
