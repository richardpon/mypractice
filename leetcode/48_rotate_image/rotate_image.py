class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix[0])
        
        for i in range(0, n):
            
            
            for x in range(0, n):
                new_row = []
                for y in range(n - 1, -1, -1):
                    cur = matrix[y][x]
                    new_row.append(cur)
            
                matrix.append(new_row)
            
                    