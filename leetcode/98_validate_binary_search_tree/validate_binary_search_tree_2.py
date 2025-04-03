# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        children are valid
        AND
        all left nodes smaller
        all right nodes larger
        """
        cur_valid, _, _ = self.is_valid_and_min_max(root)
        return cur_valid

    def is_valid_and_min_max(self,root: Optional[TreeNode]) -> tuple[bool, int, int]:
               
        cur_min = None
        cur_max = None
        if not root:
            return (True, None, None)

        left_valid, left_min, left_max = self.is_valid_and_min_max(root.left)
        right_valid, right_min, right_max = self.is_valid_and_min_max(root.right)

        # check valid first
        if not left_valid or not right_valid:
            return (False, None, None)

        if (left_max is not None and left_max >= root.val) or (right_min is not None and right_min <= root.val):

            return (False, None, None)

        cur_min = self.get_min(root.val, left_min, right_min)
        cur_max = self.get_max(root.val, left_max, right_max)

        return (True, cur_min, cur_max)


    def get_min(self, cur_val: int,left: Optional[int], right: Optional[int]) -> int:
        if left and right:
            return min(cur_val,left,right)
        elif left:
            return min(cur_val, left)
        elif right:
            return min(cur_val, right)
        else:
            return cur_val

    def get_max(self, cur_val: int,left: Optional[int], right: Optional[int]) -> int:
        if left and right:
            return max(cur_val,left,right)
        elif left:
            return max(cur_val, left)
        elif right:
            return max(cur_val, right)
        else:
            return cur_val

