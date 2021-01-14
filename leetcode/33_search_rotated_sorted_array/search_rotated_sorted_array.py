from typing import List
"""
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

(nums/target are immutable)
(nums, target, lower, upper)


length = upper - lower + 1
mid = lower + length // 2

       indexes inclusive
left = lower ... mid
right = mid+1 ...upper
            
nums            T L U
[4,5,6,7,0,1,2] 0 0 6 (length = 7, mid=3) 
[4,5,6,7,0,1,2] 0 4 6 (length = 3, mid=5)
[4,5,6,7,0,1,2] 0 4 5 (length = 2, mid=5) (special case, detect when mid==upper)
                                        left->lower..lower, right->upper..upper 
[4,5,6,7,0,1,2] 0 4 4
[4,5,6,7,0,1,2] 0 5 5

[4,5,6,7,0,1,2] 0 6 6 (one element, no match)
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        elif len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        else:
            # multiple elements
            return self.searchRecursive(nums, target, 0, len(nums) - 1)

    """
    nums, target - immutable
    lower - first element's index into nums
    upper - last element's index into nums
    """
    def searchRecursive(self, nums: List[int], target:int, lower: int, upper: int) -> int:

        # recursive base case (indexes are same)
        if upper == lower:
            # one element
            if nums[lower] == target:
                return lower
            else:
                return -1

        # multiple elements
        

        # if strictly ordered and target is out of range, stop
        # otherwise: recurse

        # check if strictly ordered (no pivot)
            # can stop if target is out of bounds
            # recursive if range contains target
        # (has pivot)
            #recurse (we can't tell)

        if nums[lower] < nums[upper] and \
            (target < nums[lower] or nums[upper] < target):
            # strictly ordered and out of range, stop
            return -1
        else:
            #recurse into both halves
            
            length = upper - lower + 1
            mid = lower + (length // 2)
            
            if mid == upper:
                left_result = self.searchRecursive(nums, target, lower, lower)
                right_result = self.searchRecursive(nums, target, upper, upper)    
            else:
                left_result = self.searchRecursive(nums, target, lower, mid)
                right_result = self.searchRecursive(nums, target, mid + 1, upper)
            

            if left_result != -1:
                return left_result
            else: 
                return right_result
