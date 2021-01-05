import unittest
from divide_two_integers import Solution
from ddt import ddt, data, unpack

@ddt
class Tester(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    @data(
        [10, 2, 5],
        [0, 1, 0],
        [10, 3, 3],
        [7, -3, -2],
        [1, 1, 1],
    )
    @unpack
    def test(self, dividend, divisor, expected):
        ret = self.s.divide(dividend,divisor)
        self.assertEqual(ret, expected)

if __name__ == '__main__':
    unittest.main()
