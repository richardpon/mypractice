"""
-maintain grid
-maintain registry of rotting fruit
-- so that the rotten fruit can spread

"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        """
        create mutable grid (recursive?)

        registry of rotten fruit
        """
        rotten = self.get_all_rotten(grid)
        rotten_candidates = []
        time = 0
        while rotten:

            if not self.any_fresh(grid):
                break

            # get all rotten candidates
            for cur_rotten_y,cur_rotten_x in rotten:
                rotten_candidates.append((cur_rotten_y+1,cur_rotten_x))
                rotten_candidates.append((cur_rotten_y-1,cur_rotten_x))
                rotten_candidates.append((cur_rotten_y,cur_rotten_x+1))
                rotten_candidates.append((cur_rotten_y,cur_rotten_x-1))

                # mark cur rotten as empty/done
                grid[cur_rotten_y][cur_rotten_x] = 0

            # apply rotten to rotten candidates
            for rotten_candidate_y,rotten_candidate_x in rotten_candidates:
                if (rotten_candidate_y >= 0 and 
                    rotten_candidate_y < len(grid) and
                    rotten_candidate_x >= 0 and
                    rotten_candidate_x < len(grid[rotten_candidate_y]) and
                    grid[rotten_candidate_y][rotten_candidate_x] == 1):
                    
                    # mark fresh as rotten
                    grid[rotten_candidate_y][rotten_candidate_x] = 2

            rotten = self.get_all_rotten(grid)

            # increment time
            time += 1


        if self.any_fresh(grid):
            return -1
        else:
            return time

    def get_all_rotten(self,grid: List[List[int]]) -> list[tuple[int,int]]:
        rotten = []
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 2:
                    rotten.append((y,x))

        return rotten        


    def any_fresh(self,grid: List[List[int]]) -> bool:
        for row in grid:
            for item in row:
                if item == 1:
                    return True

        return False


