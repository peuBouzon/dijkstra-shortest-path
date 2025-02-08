class _Node:
    def __init__(self):
        self.item = None
        self.next = None

class Bag:
    def __init__(self):
        self.first = None

    def add(self, item):
        oldFirst = self.first
        self.first = _Node()
        self.first.item = item
        self.first.next = oldFirst

    def __iter__(self):
        node = self.first
        while node is not None:
            yield node.item
            node = node.next


    

    