# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    head = None
    tail = None

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.add_helper(
            l1=l1,
            l2=l2,
            carry=0,
        )
        

    def add_helper(self,l1: Optional[ListNode], l2: Optional[ListNode], carry:int) -> Optional[ListNode]:
        if not l1 and not l2 and carry==0:
            return self.head
        
        current_value = carry
        if l1:
            current_value += l1.val
        if l2:
            current_value += l2.val


        carry=0
        if current_value > 9:
            carry = 1
            current_value -= 10

        next_node = self.add_helper(
            l1=l1.next if l1 else None,
            l2=l2.next if l2 else None,
            carry=carry,
        )

        return ListNode(
            val = current_value,
            next = next_node,
        )
