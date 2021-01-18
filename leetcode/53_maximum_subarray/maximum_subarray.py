from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        
        # start with naive way
        best_sum = None
        for subset_size in range(1, len(nums) + 1):
            cur_sum = self.max_for_size(nums, subset_size)
            if best_sum is None or cur_sum > best_sum:
                best_sum = cur_sum
        
        return best_sum

    def max_for_size(self, nums: List[int], size: int) -> int:

        cur_sum = sum(nums[0:size])
        max_sum = cur_sum
        
        #slide window
        for i in range(0, len(nums) - size):
            cur_sum -= nums[i]  # subtract prev
            cur_sum += nums[i + size] #add next

            if cur_sum > max_sum:
                max_sum = cur_sum
        
        return max_sum

