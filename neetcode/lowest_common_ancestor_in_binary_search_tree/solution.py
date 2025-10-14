# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        p_path = self.get_path(root, p)
        q_path = self.get_path(root, q)
        highest_node = None
        for i in range(min(len(p_path),len(q_path))):
            cur_p = p_path[i]
            cur_q = q_path[i]        

            if cur_p.val == cur_q.val:
                highest_node = cur_p
            else:
                break

        return highest_node




    def get_path(self, root: TreeNode, pq: TreeNode) -> list[TreeNode]:

        head = root
        path = []
        while head:
            path.append(head)
            if head.val == pq.val:
                break
            if pq.val < head.val:
                head = head.left
            else:
                head = head.right
        

        return path



