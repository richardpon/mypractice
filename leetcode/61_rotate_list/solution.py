# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        pointers to find kth and kth-1 nodes
        problem->what about large k values
            wrap around and start again at the beginning (for each pointer)

        first pointer finds the end
        second pointer finds kth node (p1=p2 for k=1, spaced by k-1 nodes)
        third point trails second be one
        """
        if not head:
            return None
        
        length_count = 1
        node = head
        while node.next:
            node = node.next
            length_count += 1
        
        k = k % length_count

        if k == 0:
            return head

        nodes_to_traverse = length_count - k
        new_head = head
        prev = None
        while nodes_to_traverse:
            prev = new_head
            new_head = new_head.next
            nodes_to_traverse -= 1        

        # detach
        prev.next = None

        # attach new
        node = new_head
        while node.next:
            node = node.next
        node.next = head
        return new_head

        




        """
        if not head:
            return None
        
        nodes:List[ListNode] = []
        cur_head = head
        while cur_head:
            nodes.append(cur_head)
            cur_head = cur_head.next

        #detach previous
        k = k % len(nodes)
        nodes[-k-1].next = None
        
        # attach new head
        new_tail = nodes[-k]
        while new_tail.next:
            new_tail = new_tail.next
        new_tail.next = head

        return nodes[-k]
        """

