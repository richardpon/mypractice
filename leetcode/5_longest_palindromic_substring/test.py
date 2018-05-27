import unittest
from longest_palindromic_substring import Solution
from ddt import ddt, data, unpack

@ddt
class TestLongestPalindrome(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    @data(
        ["a", "a"],
        ["aa", "aa"],
        ["aba", "aba"],
        ["abba", "abba"],
        ["babad", "bab"],
        ["cbbd", "bb"],
        ["abcdefcabababaksdjflskjdf", "abababa"],
        ["abcdefcababbabaksdjflskjdf", "ababbaba"],
        ["abcdefcababbbabaksdjflskjdf", "ababbbaba"],
    )

    @unpack
    def test(self, str, expected):
        # str = "abcbd"
        # expected = "bcb"
        self.assertEqual(self.s.longestPalindrome(str), expected)

if __name__ == '__main__':
    unittest.main()