import unittest
from reg_ex_matching import Solution, CharacterSymbol, DotSymbol, StarSymbol
from ddt import ddt, data, unpack

@ddt
class Tester(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    @data(
        [
            [CharacterSymbol("a")],
            [CharacterSymbol("a")]
        ],
        [
            [CharacterSymbol("a"), StarSymbol("b")],
            [CharacterSymbol("a"), StarSymbol("b")]
        ],
        [
            [CharacterSymbol("a"), StarSymbol("b"), StarSymbol("b")],
            [CharacterSymbol("a"), StarSymbol("b")]
        ],
        [
            [CharacterSymbol("a"), StarSymbol("b"), StarSymbol("b"), StarSymbol("c")],
            [CharacterSymbol("a"), StarSymbol("b"), StarSymbol("c")]
        ]

    )
    @unpack
    def test_de_dupe_symbols(self, symbols, expected):
        ret = self.s.de_dupe_stars(symbols)
        self.assertEqual(ret, expected)

    @data(
        [CharacterSymbol("a"), "a", True],
        [CharacterSymbol("a"), "b", False],
        [DotSymbol(), "b", True],
        [DotSymbol(), "h", True],
        [StarSymbol("a"), "a", True],
        [StarSymbol("a"), "b", False],
        [StarSymbol("."), "b", True],
    )
    @unpack
    def test_does_symbol_match_char(self, symbol, char, expected):
        ret = self.s.does_symbol_match_char(symbol, char)
        self.assertEqual(ret, expected)

    @data(
        ["abc", "abc", True],
        ["abc", "abcd", False],
        ["abc", "ab", False],
        ["abc_d", "abc.d", True],
        ["abc__d", "abc..d", True],
        ["abc_dd", "abc.d", False],
        ["aab", "a*b", True],
        ["aab", "c*a*b", True],
        ["mississippi", "mis*is*p*.", False],
        ["mississippi", "mis*is*ip*.", True],
        ["a", "a*", True],
        ["aaaa", "a*", True],
        ["aaaa", "a*b*", True],
        ["aaaa", ".*a*", True],
        ["aaaa", "c*.*a*", True],
        ["caaaa", "c*.*a*", True],
        ["caaaa", ".c*.*a*", True],
        ["ccaaaa", ".c*.*a*", True],
        ["ccaaaa", ".c*.*a*b*", True],
        ["ccaaaa", ".c*.*a*b*c*g*f*g*", True],
        ["ccaaaa", ".c*.*a*a*a*a*b*c*g*f*g*", True],
        ["aa", ".*", True],
        ["aaaaaaabaa", "a*a*a*a*a*a*a*a*baa", True],
        ["aa", ".*a*", True],
        ["aa", ".*a*aa*", True],
        ["aabc", ".*a*aa*b*.c*", True],
        ["aabcbc", ".*a*aa*b*.c*.*", True],
        ["aabcbcbcaccbcaabc", ".*a*aa*.*b*.c*.*", True],
        ["aabcbcbcaccbcaabc", ".*a*aa*.*b*.c*.*a*", True],
    )
    @unpack
    def test(self, s, p, expected):
        ret = self.s.isMatch(s, p)
        self.assertEqual(ret, expected)

if __name__ == '__main__':
    unittest.main()
