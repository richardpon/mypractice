class Helper:
    def __init__(self, grid: List[List[str]]):
        self.grid = grid

        # {1: {3,5}, 4:{6} }
        self.visited: dict[int, set[int]] = {}

    def explore_island(self, y:int, x:int):
        """
        visit entire island and make the adjacent cells as visited
        """
        if self.has_visited(y,x) or self.out_of_bounds(y,x):
            return

        self.visit_cell(y,x)

        if self.is_land(y,x):
            self.explore_island(y,x+1)
            self.explore_island(y,x-1)
            self.explore_island(y+1,x)
            self.explore_island(y-1,x)


    def search_islands(self) -> int:
        num_islands = 0
        # scan each unvisited cell
        # explore each island and count
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.has_visited(y,x):
                    continue        

                # explore current island
                if self.is_land(y,x):
                    self.explore_island(y,x)
                    num_islands += 1
                else:
                    # mark it as visited
                    self.visit_cell(y,x)
        
        return num_islands

    def is_land(self,y:int,x:int) -> bool:
        return self.grid[y][x] == "1"
                            
    def has_visited(self, y:int, x:int) -> bool:
        return y in self.visited and x in self.visited[y]
    
    def out_of_bounds(self,y:int, x:int) -> bool:
        return y < 0 or y >= len(self.grid) or x < 0 or x >= len(self.grid[y])
        
    def visit_cell(self, y:int, x:int) -> None:
        if y not in self.visited:
            self.visited[y] = set()
        
        self.visited[y].add(x)




class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        helper = Helper(grid)
        return helper.search_islands()
