class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #check rows
        for row in board:
            nums = self.squares_to_nums(row)
            if not self.is_valid_group(nums):
                return False
            
        #check columns
        
        for x in range(0,9):
            col = []
            for y in range(0,9):
                col.append(board[y][x])
                
            nums = self.squares_to_nums(col)
            if not self.is_valid_group(nums):
                return False
            
        #check squares
        for x_offset in range(0,3):
            for y_offset in range(0,3):
                sq = []
                for x in range(0,3):
                    for y in range(0,3):
                        real_x = x + x_offset * 3
                        real_y = y + y_offset * 3
                        sq.append(board[real_x][real_y])
                
                nums = self.squares_to_nums(sq)
                if not self.is_valid_group(nums):
                    return False
    
        return True
        
        
    def squares_to_nums(self, strings: List[str]):
        nums = []
        for s in strings:
            if s.isnumeric():
                nums.append(int(s))
        return nums
        
    def is_valid_group(self, nums: List[int]):
        deduped = set()
        for n in nums:
            if n < 1 or n > 9:
                return false
            deduped.add(n)
        
        return len(nums) == len(deduped)