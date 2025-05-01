"""
Example 1:

gas  = [1,2,3,4]
cost = [2,2,4,1]

start at 3,
gas
st -> gas
3  -> 4
0 -> 4-1+1 = 4
1 -> 4-2+2 = 4
2 -> 4-2+3 = 5
3 -> 5-4+4 = 1

O(n**2) attempt to circle from all stations 


go backwards, figure out how much gas is required to enter current station


figure out net gas
gas  = [1,2,3,4]
cost = [2,2,4,1]
net. = [-1,0,-1,3]


"""

class Helper:
    def __init__(self, gas: List[int], cost: List[int]):
        self.gas = gas
        self.cost = cost

    def can_complete_starting_at(self, index: int) -> bool:
        """
        determines if a circuit can be completed starting at the given station
        """
        cur_index = index
        num_stations_visited = 1
        gas = 0
        while num_stations_visited <= len(self.cost):
            # determine if can make it to the next station
            gas += self.gas[cur_index]
        
            # goto next station
            gas -= self.cost[cur_index]

            if gas < 0:
                return False

            cur_index += 1
            if cur_index >= len(self.gas):
                cur_index = 0
            
            num_stations_visited += 1
        
        return True


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        helper = Helper(gas, cost)
        
        for i in range(len(gas)):
            if helper.can_complete_starting_at(i):
                return i
        
        return -1


    

