import unittest
from zigzag_conversion import Solution
from ddt import ddt, data, unpack

@ddt
class TestLongestPalindrome(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    @data(
        ["ABC", 3, "ABC"],
        ["ABCDE", 3, "AEBDC"],
        ["ABCDEF", 3, "AEBDFC"],
        ["ABCDEFGHI", 3, "AEIBDFHCG"],
        ["PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"],
    )

    @unpack
    def test(self, input_string, num_rows, expected):
        self.assertEqual(self.s.convert(input_string, num_rows), expected)

if __name__ == '__main__':
    unittest.main()