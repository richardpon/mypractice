"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        # id of origiinal node to node copy
        node_id_to_copy:dict[int, Node] = {}

        cur_head = head

        # copy of original head (immutable)
        head_copy = None 
        prev_head_copy = None

        while cur_head:
            node_copy = Node(x=cur_head.val, next=cur_head.next)
            if head_copy is None:
                head_copy = node_copy

            # (still pointing to previous node)
            if prev_head_copy:
                prev_head_copy.next = node_copy

            # id of original node to node copy
            node_id_to_copy[id(cur_head)] = node_copy

            prev_head_copy = node_copy
            cur_head = cur_head.next


        old_node = head
        copy_node = head_copy
        while copy_node:
            if old_node.random:
                rand_node = node_id_to_copy[id(old_node.random)]
                copy_node.random = rand_node

            old_node = old_node.next
            copy_node = copy_node.next

        return head_copy   

      
"""


1st pass, build list of nodes to next
 - build dict from address of old node to actual new node

2nd pass - for random pointer, know the old node, get address, use dict to find new node

"""

