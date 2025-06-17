class Solution:

    def __init__(self):
        self.cache: list[list[int]] = []

    def uniquePaths(self, m: int, n: int) -> int:
        self.cache: list[list[int]] = [[0 for _ in range(n)] for _ in range(m)]
        self.cache[m-1][n-1] = 1
        return self.calc_path(0,0,m,n)
        
    def calc_path(self, y: int, x: int, m: int, n: int) -> int:

        if y >= m or x >= n:
            return 0

        if self.cache[y][x]:
            return self.cache[y][x]

        calculated_value = 0
        calculated_value += self.calc_path(y+1,x,m,n)
        calculated_value += self.calc_path(y,x+1,m,n)
        self.cache[y][x] = calculated_value
        return calculated_value

        

