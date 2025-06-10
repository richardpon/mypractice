# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.good_nodes_recursive(root, root.val)
        
    def good_nodes_recursive(self, node: TreeNode, max_so_far: int) -> int:
        
        if not node:
            return 0

        count = 0
        if node.val >= max_so_far:
            count = 1
        
        new_max = max(max_so_far, node.val)
        count += self.good_nodes_recursive(node.left, new_max)
        count += self.good_nodes_recursive(node.right, new_max)
        return count

