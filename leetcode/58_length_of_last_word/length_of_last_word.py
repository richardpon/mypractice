class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sanitized = s.strip()
        if not sanitized:
            return 0

        word_list = sanitized.split(" ")
        return len(word_list[-1])