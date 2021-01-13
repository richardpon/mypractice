from typing import List
"""
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

(nums/target are immutable)
(nums, target, lower, upper)
[4,5,6,7,  0,1,2] 0 6 (mid_index = 3) nums[0:4], nums[4:7]
left is nums[lower, mid+1]
right is nums[mid+1, upper+1]
- left is ordered, can eliminate
- right is unorder, so recurse

[4,5,6,7, 0,1 ,2] 4 6 (mid_index = 5) nums[4:6], nums[6:7]
left is ordered, is boundary, yay!
right is base case, eliminate



[4,5,6,7, 0,1,2] 0 6 (mid_index = 3) nums[0:4], nums[4:7]
- recurse into right
[0,1,2] 4 6 (mid_index = 5) nums[0:mid_index-lower+1(2)], nums[mid_index-lower+1(2):upper-lower+1(3)]
[0,1] 4 5 (mid_index = 4) nums[0:1]
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
            return self.searchRecursive(nums, target, 0, len(nums) - 1, 0)

    """
    nums, target - immutable
    lower - first element's index into nums
    upper - last element's index into nums
    """
    def searchRecursive(self, nums: List[int], target:int, lower: int, upper: int, depth: int) -> int:
        if depth == 10:
            return -1
        else:
            depth += 1

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
            """
            length = upper - lower + 1
            mid = length // 2

            left = nums[lower:mid]
            right = nums[mid:upper+1]


            length = upper - lower + 1 = 4
            mid = lower + (length / 2)
            nums=[4,5,6,7]
            left=nums[4:6]
            right=nums[6:8]


            lower = 0
            upper = 5
            [0, 1, 2, 3, 4, 5] //mid== 1
            left = nums[0:1] = [0]
            right= nums[1:3+1=4] = [1,2,3]

            lower = 0
            upper = 4
            nums=[0, 1, 2, 3, 4] //mid== 2
            left = nums[0:2] = [0,1]
            right = nums[2:4+1=5] = [2,3,4]
            # 

            [4, 5, 6, 7, 0, 1, 2] 0 4 5
            length = 5 - 4 +1 = 2
            mid = 4+1=5


            """
            length = upper - lower + 1
            mid = lower + (length // 2)
            
            if mid == upper:
                left_result = self.searchRecursive(nums, target, lower, lower, depth)
                right_result = self.searchRecursive(nums, target, upper, upper, depth)    
            else:
                left_result = self.searchRecursive(nums, target, lower, mid, depth)
                right_result = self.searchRecursive(nums, target, mid + 1, upper, depth)
            

            if left_result != -1:
                return left_result
            else: 
                return right_result
