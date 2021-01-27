# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return False
        return self.is_valid_helper(root.left, None, root.val) and self.is_valid_helper(root.right, root.val, None)

    def is_valid_helper(self, node: TreeNode, min:int, max:int) -> bool:
        if not node:
            return True
        else:
            # node.val is between min and max
            if (min is not None and node.val <= min) or (max is not None and node.val >= max):
                return False
            else:
                #apply new min/max when recursing

                #left (new max)
                left_max = node.val
                left = self.is_valid_helper(node.left, min, left_max)

                #right (new min)
                right_min = node.val
                right = self.is_valid_helper(node.right, right_min, max)

                return left and right

