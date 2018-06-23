import unittest
from longest_common_prefix import Solution
from ddt import ddt, data, unpack

@ddt
class Tester(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    @data(
        [["abc", "abc", "ab"], "ab"],
        [["abc", "abc", "ab", "a"], "a"],
        [["bc", "abc", "ab", "a"], ""],
        [["flower","flow","flight"], "fl"]

    )

    @unpack
    def test(self, strs, expected):
        ret = self.s.longestCommonPrefix(strs)
        self.assertEqual(ret, expected)

if __name__ == '__main__':
    unittest.main()
