class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0

        while True:
            if nums[i] == 0:
                return i

            next_i = nums[i]
            nums[i] = 0
            i = next_i
            
        return -1


