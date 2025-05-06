import copy
class Helper:
    def __init__(self,  board: List[List[str]]):
        self.board = board

    def check_recursive(self, word: str, y:int, x:int, visited: dict[int,set[int]]) -> bool:
        
        """
        word - what is left of word
        y - y coordinate to check
        x - x coordinate to check
        visited - y,x coordinates of cells visited
        """

        # base case
        if not word:
            return True

        # already visited
        if y in visited and x in visited[y]:
            return False

        # out of bounds check
        if y < 0 or y >= len(self.board) or x < 0 or x >= len(self.board[y]):
            return False
        
        # does not match
        if word[0] != self.board[y][x]:
            return False

        # matches, mark visited and recurse (up to four directions)
        new_word = word[1:]
        new_visited = visited
        if y not in visited:
            visited[y] = set()
        visited[y].add(x)
        
        # up, down, left, right
        return self.check_recursive(new_word, y-1,x, copy.deepcopy(new_visited)) \
        or self.check_recursive(new_word, y+1,x, copy.deepcopy(new_visited)) \
        or self.check_recursive(new_word, y,x-1, copy.deepcopy(new_visited)) \
        or self.check_recursive(new_word, y,x+1, copy.deepcopy(new_visited)) 
        

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        """
        Check if word is even possible given the available characters
           ^ is optimization needed?
        """
        helper = Helper(board)
        for y in range(len(board)):
            for x in range(len(board[y])):
                if helper.check_recursive(word, y,x,{}):
                    return True

        return False

