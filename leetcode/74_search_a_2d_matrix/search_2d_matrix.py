class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row = self.get_row(matrix, target)
        if not row:
            return False

        return self.is_element_in_row(row, target)
            

    def get_row(self, matrix: List[List[int]], target:int) -> List[int]:
        if not matrix:
            return []

        row_index = len(matrix) // 2
        row = matrix[row_index]
        if not row:
            return

        # only a single row
        if row_index == 0:
            return row

        if target < row[0]:
            return self.get_row(matrix[:row_index], target)
        else:
            return self.get_row(matrix[row_index:], target)


    def is_element_in_row(self, row: List[int],target:int) -> bool:
        if not row:
            return False
        
        index = len(row) // 2
        if target < row[index]:
            return self.is_element_in_row(row[:index], target)
        elif target == row[index]:
            return True
        else:
            return self.is_element_in_row(row[index + 1:], target)
        
            
    
