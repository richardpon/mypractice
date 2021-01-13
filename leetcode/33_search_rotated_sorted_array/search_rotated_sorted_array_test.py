import unittest
from search_rotated_sorted_array import Solution
from ddt import ddt, data, unpack

@ddt
class Tester(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    @data(
        [[4,5,6,7,0,1,2], 0, 4],
        [[4,5,6,7,0,1,2], 3, -1],
        [[4,5,6,7,0,1,2], 5, 1],
        [[1], 3, -1],
    )
    @unpack
    def test(self, nums, target, expected):
        ret = self.s.search(nums,target)
        self.assertEqual(ret, expected)

if __name__ == '__main__':
    unittest.main()
