# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
k=3 (3>2>1>4)

cur = head
caboose = head
next = head.next
move caboose k nodes (can be none for last node), if can't, then done
head = 1 (update later at end of moving cur k group, this can be recursive)

1 -> 2 -> 3 -> 4 (cur = 1, next = 2, caboose = 4, nodes_to_move=3)
cur.next = caboose
caboose = cur
cur = next
next = next.next

2 -> 3 -> 4 (cur = 2, next = 3, caboose = 1, nodes_to_move=2)
     1 ->

cur.next = caboose
caboose = cur
cur = next
next = next.next 

     3 -> 4 (cur = 3, next = 4, caboose = 2, nodes_to_move=1)
2 -> 1 -> 

cur.next = caboose
caboose = cur
cur = next
next = next.next 

3 -> 2 -> 1 -> 4 (cur = 4, next = None, caboose = 3, nodes_to_move=0)

set head to caboose after moving complete kgroup if first kgroup moved,
otherwise, no need to change head



"""

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        