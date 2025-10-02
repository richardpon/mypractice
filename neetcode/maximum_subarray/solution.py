class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_so_far = nums[0]
        running_max = nums[0]

        for num in nums[1:]:
            cur_max = running_max + num

            if cur_max > max_so_far:
                max_so_far = cur_max

            running_max = max(cur_max, num)

        return max(max_so_far, running_max)

