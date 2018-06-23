class Solution:
    def longestCommonPrefix(self, strs):

        longest_prefix = ""

        if len(strs) == 0:
            return longest_prefix

        for i in range(0, len(strs[0])):
            cur_char = strs[0][i]

            for s in strs[1:]:
                if i >= len(s) or cur_char != s[i]:
                    return longest_prefix

            longest_prefix += cur_char

        return longest_prefix
