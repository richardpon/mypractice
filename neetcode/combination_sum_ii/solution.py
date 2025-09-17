class Solution:
    def __init__(self):
        # unique ordered tuples
        self.combos: set[tuple[int]] = set()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sorted_nums = sorted(candidates)
        self.search_sum(sorted_nums, target, [])
        
        output = [list(combo) for combo in self.combos]
        return output

    def search_sum(self, candidates: List[int], target:int, so_far:List[int]) -> None:
        
        if target == 0:
            combo = sorted(so_far)
            self.combos.add(tuple(combo))
            return
        
        if not candidates:
            return

        first = candidates[0]
        if first > target:
            return 

        self.search_sum(candidates[1:], target - first, so_far + [first])
        self.search_sum(candidates[1:], target, so_far)


