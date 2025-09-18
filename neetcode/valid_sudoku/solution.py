class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return (
            self.has_valid_rows(board) and
            self.has_valid_columns(board) and
            self.has_valid_boxes(board)
            )

    def has_valid_rows(self, board: List[List[str]]) -> bool:
        for row in board:
            so_far = set()
            for num in row:
                if num.isdigit() and num in so_far:
                    return False
                so_far.add(num)
        return True

    def has_valid_columns(self, board: List[List[str]]) -> bool:
        for j in range(9):
            so_far = set()
            for i in range(9):
                num = board[i][j]
                if num.isdigit() and num in so_far:
                    return False
                so_far.add(num)
        return True


    def has_valid_boxes(self, board: List[List[str]]) -> bool:
        buckets = [[set() for _ in range(3)] for _ in range(3)]
        
        for i in range(9):
            row = board[i]

            for j in range(9):
                cur_bucket = buckets[i // 3][j // 3]

                num = board[i][j]
                if num.isdigit():
                    if num in cur_bucket:
                        return False
                
                    cur_bucket.add(num)

        return True

