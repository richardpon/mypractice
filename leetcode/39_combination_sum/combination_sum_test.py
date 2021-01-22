import unittest
from combination_sum import Solution
from ddt import ddt, data, unpack

@ddt
class Tester(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    @data(
        [ [2,3,6,7], 7, [[7], [2,2,3]] ],
        [ [2,3,5], 8, [ [2,3,3], [2,2,2,2], [3,5]] ]
    )
    @unpack
    def test(self, nums, target, expected):
        ret = self.s.combinationSum(nums,target)
        self.assertEqual(ret, expected)

if __name__ == '__main__':
    unittest.main()
