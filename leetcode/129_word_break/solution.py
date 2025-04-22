class Solution:

    def __init__(self):
        self.is_matched: dict[str, bool] = {}
        

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.word_break_recursive(s, wordDict)
        

    def word_break_recursive(self, s: str, wordDict: List[str]) -> bool:

        if len(s) == 0:
            return True
        
        # Check if we already computed a (not)match
        if s in self.is_matched:
            return self.is_matched[s]
        
        # Check word in dict if s starts with it
        for word in wordDict:
            if s.startswith(word):
                # remove word from s and recurse
                new_word_to_check = s[len(word):]
                new_word_matched = self.wordBreak(new_word_to_check, wordDict)
                self.is_matched[new_word_to_check] = new_word_matched
                if new_word_matched:
                    return True

        return False

