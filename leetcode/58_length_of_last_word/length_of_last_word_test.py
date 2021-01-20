import unittest
from length_of_last_word import Solution
from ddt import ddt, data, unpack

@ddt
class Tester(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    @data(
        ["hello world", 5],
        ["hello o 00 000", 3],
        [" ", 0],
        ["   ", 0],
        ["  a ", 1],
    )
    @unpack
    def test(self, s, expected):
        ret = self.s.lengthOfLastWord(s)
        self.assertEqual(ret, expected)

if __name__ == '__main__':
    unittest.main()
