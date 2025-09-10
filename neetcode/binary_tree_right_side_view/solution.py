# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        return self.right_side_nodes([root])

    def right_side_nodes(self, nodes: list[TreeNode]) -> List[int]:
        if not nodes:
            return []

        nodes_at_next_level:list[TreeNode] = []
        right_most_node: int|None = None

        for node in nodes:
            if not node:
                continue
            if node.left:
                nodes_at_next_level.append(node.left)
            if node.right:
                nodes_at_next_level.append(node.right)
            
            right_most_node = node.val
        
        return [right_most_node] + self.right_side_nodes(nodes_at_next_level)


