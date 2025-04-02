# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class NodeWithLevel:
    node: TreeNode
    level: int

    def __init__(self,node,level):
        self.node = node
        self.level = level


class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        current_level_values = []

        queue = [NodeWithLevel(node=root, level=0)]
        current_level = 0

        while queue:
            head = queue[0]
            queue = queue[1:]

            if not head or not head.node:
                continue
            
            if head.level == current_level:
                current_level_values.append(head.node.val)
            else:
                # increments level
                current_level = head.level
                
                # add previous level values to output
                output.append(current_level_values)
                
                # reset current level values
                current_level_values=[head.node.val]

            # recurse
            queue.append(NodeWithLevel(node=head.node.left, level=current_level+1))
            queue.append(NodeWithLevel(node=head.node.right, level=current_level+1))

        if current_level_values:
            output.append(current_level_values)
        return output

