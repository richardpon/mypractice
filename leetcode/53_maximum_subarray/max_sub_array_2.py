from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        running_total = 0
        best_sum = None

        for num in nums:
            # each num may be individually the best
            if best_sum is None or num > best_sum:
                best_sum = num
            
            if num > 0:
                # positive numbers
                if running_total > 0:
                    running_total += num
                else:
                    running_total = num
            else:
                # negative numbers
                running_total += num

        
            # maybe update best_sum with running total if better
            if running_total > best_sum and running_total > 0:
                best_sum = running_total

        return best_sum

