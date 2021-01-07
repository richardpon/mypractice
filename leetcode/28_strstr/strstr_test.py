import unittest
from strstr import Solution
from ddt import ddt, data, unpack

@ddt
class Tester(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    @data(
        ["hello", "ll", 2],
        ["hello", "o", 4],
        ["abc", "", 0],
        ["aaaaa", "bba", -1],
        ["a", "a", 0]
        
    )
    @unpack
    def test(self, haystack, needle, expected):
        ret = self.s.strStr(haystack,needle)
        self.assertEqual(ret, expected)

if __name__ == '__main__':
    unittest.main()
