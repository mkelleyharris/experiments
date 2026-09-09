
import unittest

def even_numbers(low, hi):
    return [x for x in range(low, hi+1) if ((x % 2) == 0)]

class TestEvenNumbers(unittest.TestCase):

    def test_even_numbers(self):
        self.assertEqual([0, 2, 4], even_numbers(0, 5))
        self.assertEqual([2, 4, 6, 8], even_numbers(1, 9))
        self.assertEqual([94, 96, 98], even_numbers(93, 99))

if __name__ == '__main__':
    print even_numbers(1, 99)

    l1 = [ 1, 2, "frog"]
    print l1
    unittest.main()

