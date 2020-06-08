import unittest

from src.ThreeSum import ThreeSum


class MyTestCase(unittest.TestCase):
    def test_empty_input(self):
        threesum = ThreeSum([])
        self.assertEqual([], threesum.find())

    def test_single_input(self):
        threesum = ThreeSum([1])
        self.assertEqual([], threesum.find())

    def test_double_input(self):
        threesum = ThreeSum([1,2])
        self.assertEqual([], threesum.find())

    def test_3zeroes_input(self):
        threesum = ThreeSum([0,0,0])
        self.assertEqual([[0,0,0]], threesum.find())

    def test_one(self):
        threesum = ThreeSum([-1, 0, 1, 2, -1, -4])
        self.assertCountEqual([[-1,0,1],[-1,-1,2]], threesum.find())

    def test_two(self):
        threesum = ThreeSum([1, -1, -1, 0])
        self.assertCountEqual([[1,-1,0]], threesum.find())

if __name__ == '__main__':
    unittest.main()
