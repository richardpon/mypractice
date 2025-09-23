class Region:
    ignored:set[tuple[int,int]]

    def __init__(self,board: List[List[str]]):
        self.board = board
        self.ignored = set()
    
    def mark_off_island(self, y:int, x:int) -> None:

        """
        identify all cells that are part of the island connected to cell at y,x
        if the island is surrounded, capture it
        if the island touches the edge, ignore it
        """
        island:set[tuple[int]] = {(y,x)}
        cells_to_check = [(y,x)]
        can_be_captured = True
        already_checked = set()
    
        while cells_to_check:
            y,x = cells_to_check.pop()

            if (y,x) in already_checked:
                continue
            already_checked.add((y,x))


            if not self.is_inside_board(y,x):
                continue

            if self.board[y][x] == 'X':
                continue

            # on the board, and an O
            island.add((y,x))

            if self.is_on_edge(y,x):
                can_be_captured = False

            # traverse
            cells_to_check.append((y,x-1))
            cells_to_check.append((y,x+1))
            cells_to_check.append((y+1,x))
            cells_to_check.append((y-1,x))
        
        if can_be_captured:
            for y,x in island:
                self.board[y][x] = 'X'

        self.ignored.add((y,x))
                

    
    def is_on_edge(self, y:int, x:int) -> bool:
        return (y == 0 or 
            y == len(self.board) - 1 or
            x == 0 or
            x == len(self.board[0]) - 1
        )
    
    def is_inside_board(self, y:int, x:int) -> bool:
        return (y >= 0 and
        y < len(self.board) and
        x >= 0 and
        x < len(self.board[0])
        )

    

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        scan to find region part
        once find part of region, 
          determine all region cells
          determine if surrounded, or touch edge

          if surrounded, mark as captured
          if not surrounded, mark as ignore

        """

        h = len(board)
        w = len(board[0])

        region = Region(board)
        for y, row in enumerate(board):
            for x, cell in enumerate(row):
                if (y,x) in region.ignored:
                    continue
                if cell == 'O':
                    region.mark_off_island(y,x)
        
