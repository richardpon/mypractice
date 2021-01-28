from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
flatten the tree

[1, 2, 2, 3, 4, 4, 3]

"""

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        left = self.flatten(root.left, True)
        right = self.flatten(root.right, False)

        return left == right

    
    def flatten(self, node: TreeNode, flipped: bool) -> List[int]:
        if not node:
            return [None]
        
        if flipped:
            return [node.val] + self.flatten(node.right, flipped) + self.flatten(node.left, flipped) 
        else:
            return [node.val] + self.flatten(node.left, flipped) + self.flatten(node.right, flipped) 

