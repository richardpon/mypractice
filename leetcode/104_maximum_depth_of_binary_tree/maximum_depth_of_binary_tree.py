# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        # breadth first search
        queue = []
        depths = []
        queue.append(root)
        depths.append(1)
        max_depth = 0

        while queue:
            cur = queue.pop(0)
            cur_depth = depths.pop(0)

            if cur:
                max_depth = max(max_depth, cur_depth) 
                queue.append(cur.left)
                depths.append(cur_depth + 1)
                queue.append(cur.right)
                depths.append(cur_depth + 1)
        
        return max_depth

