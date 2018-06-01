import unittest
from palindrome_number import Solution
from ddt import ddt, data, unpack

@ddt
class TestPalindromeNumber(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    @data(
        [121, True],
        [-121, False],
        [10, False],
        [10101, True],
        [101101, True],
    )

    @unpack
    def test(self, input, expected):
        self.assertEqual(self.s.isPalindrome(input), expected)

if __name__ == '__main__':
    unittest.main()