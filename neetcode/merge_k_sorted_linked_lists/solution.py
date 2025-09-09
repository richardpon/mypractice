# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        
        tail = lists[2:]
        merged = self.merge_lists(lists[0], lists[1])
        
        return self.mergeKLists([merged] + tail)


    def merge_lists(self, first:Optional[ListNode], second:Optional[ListNode]) -> Optional[ListNode]:
        if first is None:
            return second
        elif second is None:
            return first
        
        if first.val < second.val:
            head = first
            first = first.next
        else:
            head = second
            second = second.next
    
        head.next = self.merge_lists(first,second)
        return head
