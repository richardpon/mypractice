class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.search_recursive(nums,target,0, len(nums)-1)

    def search_recursive(self, nums: List[int], target: int, left:int, right:int) -> int:
        if left == right:
            return left if nums[left] == target else -1
        
        if not self.is_rotated(nums, left, right):
            if target < nums[left] or nums[right] < target:
                return -1
            
        mid = (left + right) // 2

        left_position = self.search_recursive(nums, target, left, mid)
        if left_position != -1:
            return left_position
        
        return self.search_recursive(nums, target, mid + 1, right)

    def is_rotated(self, nums: List[int],left:int, right:int) -> bool:
        return nums[left] > nums[right]
        
