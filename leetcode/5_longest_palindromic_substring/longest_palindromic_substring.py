class Solution:

    def longestPalindrome(self, s):
        longest_so_far = ""

        for i in range(0, len(s)):
            # single
            p = self.get_palindrome(i, i, "", s)
            if len(p) > len(longest_so_far):
                longest_so_far = p

            if i + 1 < len(s):
                p = self.get_palindrome(i, i + 1, "", s)
                if len(p) > len(longest_so_far):
                    longest_so_far = p

        return longest_so_far

    # Given to indexes of the string
    # Assumes both indexes are valid
    def get_palindrome(self, i, j, pal_so_far, s):

        # print("get_palindrome({},{},{},{})".format(i, j, pal_so_far, s))

        if s[i] == s[j]:
            if i == j:
                pal_so_far = s[i]
            else:
                pal_so_far = s[i] + pal_so_far + s[j]

            if i > 0 and j < len(s) - 1:
                i -= 1
                j += 1
                return self.get_palindrome(i, j, pal_so_far, s)
            else:
                return pal_so_far
        else:
            return pal_so_far
