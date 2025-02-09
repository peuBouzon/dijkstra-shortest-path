import unittest
from priorityqueue import MinIndexPriorityQueue
import random

class TestMinPriorityQueue(unittest.TestCase):

    def test_pop_min_item(self):
        numbers = [random.randint(-100, 100) for _ in range(10000)]

        self.pq = MinIndexPriorityQueue(len(numbers))
        for i, number in enumerate(numbers):
            self.pq.insert(i + 1, number)
        sorted_numbers = sorted(numbers)
        i = 0
        while self.pq:
            self.assertEqual(sorted_numbers[i], self.pq.pop()[1])
            i += 1

    def test_change(self):
        self.pq = MinIndexPriorityQueue(4)
        for i in range(1, 4):
            self.pq.insert(i, i)

        self.pq.change(2, -1) # now the second element is the smallest
        min_index, min = self.pq.pop()
        self.assertEqual(min_index, 2)
        self.assertEqual(min, -1)

    def test_contains(self):
        self.pq = MinIndexPriorityQueue(1)
        self.assertFalse(self.pq.contains(1))
        self.pq.insert(1, 1)
        self.assertTrue(self.pq.contains(1))

    def test_increment_size_with_push(self):
        self.pq = MinIndexPriorityQueue(2)
        self.pq.insert(1, 1)
        old_size = len(self.pq)
        self.pq.insert(2, 2)
        self.assertEqual(old_size + 1, len(self.pq))

    def test_queue_max_size(self):
        self.assertRaises(ValueError, lambda : MinIndexPriorityQueue(0))

    def test_push_into_full_queue(self):
        self.pq = MinIndexPriorityQueue(1)
        self.pq.insert(1, 1)
        self.assertRaises(MinIndexPriorityQueue.QueueFull, lambda : self.pq.insert(2, 2))

    def test_decrement_size_with_pop(self):
        self.pq = MinIndexPriorityQueue(2)
        self.pq.insert(1, 1)
        self.pq.insert(2, 2)
        old_size = len(self.pq)
        self.pq.pop()
        self.assertEqual(old_size - 1, len(self.pq))

    def test_pop_with_empty_queue(self):
        self.pq = MinIndexPriorityQueue(2)
        self.assertRaises(MinIndexPriorityQueue.QueueEmpty, lambda : self.pq.pop())

if __name__ == '__main__':
    unittest.main()