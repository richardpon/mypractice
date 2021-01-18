import unittest
from maximum_subarray import Solution
from ddt import ddt, data, unpack

@ddt
class Tester(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    @data(
        [[1], 1],
        [[-2,1,-3,4,-1,2,1,-5,4], 6],
        [[-2,-1],-1],
        [[0,-1],0]
    )
    @unpack
    def test(self, nums, expected):
        ret = self.s.maxSubArray(nums)
        self.assertEqual(ret, expected)

    @data(
        [[1,5,2,4,3], 1, 5],
        [[0,-2], 2, -2],
        [[0,-2], 1, 0],
        [[-1,0], 1, 0],
        [[0,-1], 1, 0],
    )
    @unpack
    def test_max_for_size(self, nums, size, expected):
        ret = self.s.max_for_size(nums,size)
        self.assertEqual(ret, expected)

if __name__ == '__main__':
    unittest.main()
