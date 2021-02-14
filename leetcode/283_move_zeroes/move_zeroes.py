class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        num_zeroes = 0
        i = 0
        while i < len(nums):
            cur = nums[i]
            
            if cur == 0:
                num_zeroes += 1
                del nums[i] #keep i, numbers shift to left
            else:
                i += 1
                
        for i in range(0, num_zeroes):
            nums.append(0)
            