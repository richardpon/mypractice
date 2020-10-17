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

    def __str__(self):
        if self.val is None:
            return "None"
        else:
            return str(self.val)

    """
    Case 1: Remove nth node (not the first node):
    n=1, target to remove (3)
    (1)->(2)->(3)-> n=1, tb=0
    HTI

    (1)->(2)->(3)-> n=1, tb=1
    HT    I

    (1)->(2)->(3)-> n=1, tb=1
    H     T    I
    n==tb and I.next is None, set t.next=t.next.next, returns (1)->(2)->


    n=2, target to remove (2)
    (1)->(2)->(3)-> n=2, tb=0
    HTI

    (1)->(2)->(3)-> n=2, tb=1
    HT    I

    (1)->(2)->(3)-> n=2, tb=2
    HT         I
    n==tb and I.next is None, set t.next=t.next.next, returns (1)->(3)->


    Case 2: Remove 1st node
    n=1, target remove (1)
    (1)->   n=1,tb=0
    HTI

    if I.next is None and n-tb==1, remove 1st node, return H.next=None

    n=2, target to remove (1)
    (1)->(2)->  n=2,tb=0
    HTI

    (1)->(2)->  n=2,tb=1
    HT    I
    I.next is None and n-tb==1, remove 1st node, return H.next= (2)->


    Case 3: Invalid node to remove
    n=10
    (1)->   n=10, tb=0
    HTI
    I.next is None and n-tb > 1, return head (don't remove any node)


    """

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return head

        trailing_by = 0
        incrementing_node = head
        trailing_node = head

        # increment incrementing_node until trailing_by == n
        while trailing_by < n:
            # Can I increment
            if incrementing_node.next:
                # yes, safe to increment
                incrementing_node = incrementing_node.next
                trailing_by += 1
            else:
                # can't increment, hit end of list
                if n - trailing_by == 1:
                    # Remove 1st node
                    return head.next
                else:
                    # can't remove any nodes, n is too high
                    return head
        
        # we know trailing_by == n
        # increment both incrementing_node and trailing_node until hit end of list
        while incrementing_node.next:
            incrementing_node = incrementing_node.next
            trailing_node = trailing_node.next

        # at end of list
        trailing_node.next = trailing_node.next.next
        return head
        
    