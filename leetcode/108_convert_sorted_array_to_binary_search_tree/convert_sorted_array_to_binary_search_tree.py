# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        
        #at least one element
        middle_index = len(nums) // 2
        middle_element = nums[middle_index]

        left = self.sortedArrayToBST(nums[0:middle_index])
        right = self.sortedArrayToBST(nums[middle_index + 1:])

        return TreeNode(middle_element, left, right)
