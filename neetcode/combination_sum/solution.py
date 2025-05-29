class Solution:

    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums = sorted(nums)
        combos = self.combo(nums, target, [])
        combos_sorted =  [(sorted(combo)) for combo in combos]
        combo_set = set([tuple(combo) for combo in combos_sorted])
        return [list(combo) for combo in combo_set]


    def combo(self,nums:list[int], target:int, so_far:list[int]) -> list[list[int]]:
        if target < 0:
            return []
        
        if target == 0:
            return [so_far]
        
        out = []
        for num in nums:
            cur_result = self.combo(nums, target - num, so_far + [num])

            if cur_result:
                out = out + cur_result

        return out


