
import unittest

def remove_duplicates(alist):
    return list(set(alist))

class TestSet(unittest.TestCase):

    def test_even_numbers(self):
        self.assertEqual([1, 2], remove_duplicates([1, 2]))
        self.assertEqual([2], remove_duplicates([2, 2, 2]))
        self.assertEqual([1, 2, 3, 4], remove_duplicates([1, 2, 2, 3, 3, 4]))

if __name__ == '__main__':
    unittest.main()

