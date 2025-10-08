# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
            
        if k == 1:
            return head

        # find new head
        new_tail = head
        new_head = head
        for _ in range(k-1):
            if not new_head.next:
                return head
            new_head = new_head.next


        trailer = None
        next_node = None # temp ref
        cur_head = head

        while cur_head is not new_head:
            next_node = cur_head.next
            
            if trailer is None:    
                cur_head.next = new_head.next
            else:
                cur_head.next = trailer

            trailer = cur_head
            cur_head = next_node

        new_tail.next = self.reverseKGroup(new_head.next, k)
        new_head.next = trailer

        return new_head


