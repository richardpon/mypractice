import unittest
from max_number_of_ksum_pairs import Solution
from ddt import ddt, data, unpack

@ddt
class Tester(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    @data(
        [[1,2,3,4], 5, 2],
        [[1],1, 0],
        [[3,1,3,4,3],6,1]
    )
    @unpack
    def test(self, nums, k, expected):
        ret = self.s.maxOperations(nums, k)
        self.assertEqual(ret, expected)

if __name__ == '__main__':
    unittest.main()
