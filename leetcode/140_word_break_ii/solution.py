class Helper:
    def __init__(self,wordDict: List[str]): 
        """
        # set of words that can't be broken
        # example 3:
        # {
            "catsandod": [],
            }
        #self.non_words:set[str] = set()

        
        mapping of valid (sub)words to output sentences
        example 1:
        {
            "catsanddog": [
                "cats and dog",
                "cat sand dog",
            ]
        }

        EXAMPLE 1:
        cat/cats in catsanddog
        add "cat" to "sanddog"
        add "cats" to "anddog"
        
        no add "and to ___

        if current dict word starts s, (yes match), need to see if subword has any matches, if so, pre-pend

        """
        self.words_to_sentences:dict[str,list[str]] = {}
        self.wordDict = wordDict

    # multiple sentences (sets) can be found
    def word_break(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        
        if s in self.words_to_sentences:
            return self.words_to_sentences[s] #list[str]

        self.words_to_sentences[s] = []

        # can have multiple matches (multiple words can create valid sentencese)
        #sentences_for_cur_word: List[str] = []
        
        # finding all the sentences (recursively, for the current word)
        for word in self.wordDict:
            if s.startswith(word):
                
                # exact match
                if s == word:
                    self.words_to_sentences[s].extend([word])
                else:   
                    # not exact match, need to recurse into children
                    sub_sentences = self.word_break(s[len(word):])

                    new_sub_sentences: List[str] = [word + " " + sub for sub in sub_sentences]
            
                    self.words_to_sentences[s].extend(new_sub_sentences)

        return self.words_to_sentences[s]
                               

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        helper = Helper(wordDict)
        return helper.word_break(s)

