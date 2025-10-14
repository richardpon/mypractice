class Solution:
    def __init__(self):
        # number of steps left -> # ways
        self.lookup: dict[int,int] = {
            1:1,
            2:2,
        }

    def climbStairs(self, n: int) -> int:

        if n in self.lookup:
            return self.lookup[n]

        # 1 or 2
        num_ways_one = self.climbStairs(n - 1)
        num_ways_two = self.climbStairs(n - 2)

        # record # ways
        num_ways = num_ways_one + num_ways_two

        self.lookup[n] = num_ways

        return num_ways
