import unittest
from bag import Bag

import random

class TestBag(unittest.TestCase):
    def test_add(self):
        numbers = [random.randint(-100, 100) for _ in range(10000)]

        bag = Bag()
        for number in numbers:
            bag.add(number)

        bag_numbers = [x for x in bag]
        self.assertEqual(len(bag_numbers), len(numbers))
        self.assertEqual(set(bag_numbers), set(numbers))

if __name__ == '__main__':
    unittest.main()