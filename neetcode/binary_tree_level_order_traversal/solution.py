# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    
        queue:list[tuple[int, TreeNode]] = []
        output:list[list[int]] = []

        if not root:
            return []

        queue.append((0,root))

        while queue:
            level, node = queue[0]
            queue = queue[1:]

            if not node:
                continue

            if level >= len(output):
                output.append([node.val])
            else:
                output[level].append(node.val)

            queue.append((level+1, node.left))
            queue.append((level+1, node.right))

        return output

