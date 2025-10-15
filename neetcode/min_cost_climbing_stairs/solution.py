class Solution:
    def __init__(self):
        # floor -> min_total_cost
        self.cost_from_floor: dict[int,int] = {}

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return min(self.min_cost(cost, 0),self.min_cost(cost, 1));


    def min_cost(self,  cost: List[int], floor:int) -> int:
        if floor >= len(cost):
            return 0
        
        if floor in self.cost_from_floor:
            return self.cost_from_floor[floor]

        cost_jump_1 = self.min_cost(cost, floor+1)
        cost_jump_2 = self.min_cost(cost, floor+2)

        cur_cost = cost[floor] + min(cost_jump_1, cost_jump_2)

        self.cost_from_floor[floor] = cur_cost
        return cur_cost

