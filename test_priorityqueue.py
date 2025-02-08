import unittest
from priorityqueue import MinPriorityQueue
import random

class TestMinPriorityQueue(unittest.TestCase):

    def test_pop_min_item(self):

        numbers = [random.randint(-100, 100) for _ in range(100000)]

        self.priority_queue = MinPriorityQueue(len(numbers))
        for number in numbers:
            self.priority_queue.push(number)

        popped_numbers = []
        while self.priority_queue:
            popped_numbers.append(self.priority_queue.pop())

        self.assertEqual(popped_numbers, sorted(numbers))

    def test_increment_size_with_push(self):
        self.priority_queue = MinPriorityQueue(2)
        self.priority_queue.push(1)
        old_size = len(self.priority_queue)
        self.priority_queue.push(2)
        self.assertEqual(old_size + 1, len(self.priority_queue))

    def test_push_into_full_queue(self):
        self.priority_queue = MinPriorityQueue(0)
        self.assertRaises(MinPriorityQueue.QueueFull, lambda : self.priority_queue.push(1))

        self.priority_queue = MinPriorityQueue(1)
        self.priority_queue.push(1)
        self.assertRaises(MinPriorityQueue.QueueFull, lambda : self.priority_queue.push(2))

    def test_decrement_size_with_pop(self):
        self.priority_queue = MinPriorityQueue(2)
        self.priority_queue.push(1)
        self.priority_queue.push(2)
        old_size = len(self.priority_queue)
        self.priority_queue.pop()
        self.assertEqual(old_size - 1, len(self.priority_queue))

    def test_pop_with_empty_queue(self):
        self.priority_queue = MinPriorityQueue(0)
        number = self.priority_queue.pop()
        self.assertIsNone(number)

if __name__ == '__main__':
    unittest.main()