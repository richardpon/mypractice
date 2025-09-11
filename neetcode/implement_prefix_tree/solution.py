class PrefixTree:

    def __init__(self):
        self.children: dict[str, PrefixTree] = {}
        self.is_leaf: bool = False

    def insert(self, word: str) -> None:
        if not word:
            return None

        char = word[0]
        if char not in self.children:
            self.children[char] = PrefixTree()

        if len(word) == 1:
            self.children[char].is_leaf = True
        
        self.children[char].insert(word[1:])


    def search(self, word: str) -> bool:
        if not word:
            return self.is_leaf
        
        char = word[0]
        if char not in self.children:
            return False
        
        return self.children[char].search(word[1:])

        
    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return True
        
        char = prefix[0]
        if char not in self.children:
            return False
        
        return self.children[char].startsWith(prefix[1:])
        
