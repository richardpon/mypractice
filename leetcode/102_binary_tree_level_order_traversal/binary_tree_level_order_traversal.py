from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = []
        depth = []

        output = [[]]
        if not root:
            return []
        
        queue.append(root)
        depth.append(0)
        prev_depth = 0

        while queue:
            cur_node = queue.pop(0)
            cur_depth = depth.pop(0)

            if cur_node:
                # is this node at a new depth?
                if cur_depth != prev_depth:
                    #new depth
                    output.append([cur_node.val])
                    prev_depth = cur_depth
                else:
                    # same depth
                    output[-1].append(cur_node.val)

                queue.append(cur_node.left)
                depth.append(cur_depth + 1)

                queue.append(cur_node.right)
                depth.append(cur_depth + 1)
        
        return output


