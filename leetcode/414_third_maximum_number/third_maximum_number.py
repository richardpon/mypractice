class Solution:
    def __init__(self):
        self.distinct_maxes = set()
        self.sorted_maxes = []

    def thirdMax(self, nums: List[int]) -> int:
        for num in nums:
            self.maybe_add_to_maxes(num)
        
        if len(self.sorted_maxes) == 3:
            return self.sorted_maxes[0] 
        else:
            return self.sorted_maxes[-1]

    def maybe_add_to_maxes(self, current:int) -> None:
        if current in self.distinct_maxes:
            return

        new_maxes = self.sorted_maxes
        new_maxes.append(current)
        new_sorted_maxes = sorted(new_maxes)
        
        if len(new_sorted_maxes) > 3:
            new_sorted_maxes = new_sorted_maxes[1:]

        self.sorted_maxes = new_sorted_maxes
        self.distinct_maxes = set(new_sorted_maxes)


