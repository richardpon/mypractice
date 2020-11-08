from typing import List

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


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # Merge first two lists and put at end
        # recurse

        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        else:
            mergedList = self.mergeTwo(lists[0], lists[1])
            return self.mergeKLists(lists[2:] + [mergedList])

    def mergeTwo(self, a: ListNode, b: ListNode) -> ListNode:

        if not a:
            return b
        elif not b:
            return a
        else:
            if a.val < b.val:
                head = a
                tail = self.mergeTwo(a.next, b)
            else:
                head = b
                tail = self.mergeTwo(a, b.next)
            head.next = tail
            return head
