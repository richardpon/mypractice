class Solution:
    def isPalindrome(self, x):
        s = str(x)
        for i in range(0, int(len(s) / 2) + 1):
            if s[i] != s[len(s) - i - 1]:
                return False

        return True
