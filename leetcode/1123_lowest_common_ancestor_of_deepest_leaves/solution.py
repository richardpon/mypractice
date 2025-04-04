# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.deepest_leaves:list[int] = []
        self.max_depth = None
        self.leaf_to_parent: dict[int, int] = {}
        self.val_to_leaf: dict[int, TreeNode] = {}

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.find_deepest_leaves(root, 0)

        parent_val =  self.find_common_parent(self.deepest_leaves)
        
        return self.val_to_leaf[parent_val]

    def find_deepest_leaves(self, root: Optional[TreeNode], depth: int):
        """
        populates self.deepest_leaves with list of leaves at deepest depth
        """
        if not root:
            return
        self.val_to_leaf[root.val] = root

        if self.max_depth is None:
            self.max_depth = depth
            self.deepest_leaves = [root.val]
        elif depth == self.max_depth:
            self.deepest_leaves.append(root.val)
        elif depth > self.max_depth:
            self.max_depth = depth
            self.deepest_leaves = [root.val]
        
        # None as key is ok
        if root.left:
            self.leaf_to_parent[root.left.val] = root.val
            self.find_deepest_leaves(root.left, depth + 1)
        if root.right:
            self.leaf_to_parent[root.right.val] = root.val
            self.find_deepest_leaves(root.right, depth + 1)


    def find_common_parent(self, leaves:list[int]) -> int:
        """
        Finds common parent amongst self.deepest_leaves

        Assumes a single common parent if multiple leaves in self.deepest_leaves
        """
        if len(leaves) == 1:
            return leaves.pop()
        
        parents = set()
        for leaf in leaves:
            cur_parent = self.leaf_to_parent[leaf]
            parents.add(cur_parent)
        
        return self.find_common_parent(parents)


