from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def toList(self) -> List[int]:
        if self.next is not None:
            tailList = self.next.toList()
        else:
            tailList = []
        return [self.val] + tailList
    
    def __str__(self) -> str:
        return str(self.val)


"""
each iteration
put lowest of l1.val or l2.val onto output
move lowest to out, increment l1/l2

"""

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        tail = None
    
        while l1 or l2:
            nextNode, l1, l2 = self.getLowestNode(l1, l2)

            if not head:
                head = nextNode
                tail = nextNode
            else:
                tail.next = nextNode
                tail = nextNode

        return head


    """
    return ListNode containing smaller value of l1 or l2.
    pops the node off l1 or l2
    """
    def getLowestNode(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        elif not l1:
            lower = l2
            l2 = None 
        elif not l2:
            lower = l1
            l1 = None
        elif l1.val < l2.val:
            lower = l1
            l1= l1.next
        else:
            lower = l2
            l2 = l2.next
        return lower, l1, l2