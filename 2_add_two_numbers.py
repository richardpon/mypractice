# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


'''
    Cases
    L1 and L2 have a next (and maybe a carry)
    only L1 OR L2 have a next (maybe. carry) (convert carry to ListNode)
    no next ( but maybe carry ) ( convert to a list node) (can convert to two list nodes)

'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        s = "{}".format(self.val)
        if self.next != None:
            s += " -> " + repr(self.next)
        return s


class RecursiveSolution:

    def addTwoNumbers(self, aa, bb):
        return self.addTwoWithCarry(aa, bb, 0)
        
    # returns ListNode
    # l1 and l2 may be defined
    def addTwoWithCarry(self, l1, l2, c):
        
        #l1 and l2 are defined
        if l1 != None and l2 != None:
            # calc val
            curVal = l1.val + l2.val + c
            if curVal > 9:
                actualVal = curVal - 10
                carry = 1
            else:
                actualVal = curVal
                carry = 0

            newNode = ListNode(actualVal)
            newNode.next = self.addTwoWithCarry(l1.next, l2.next, carry)
            return newNode

        #only l1 OR l2 is defined
        elif l1 != None or l2 != None:
            #val
            if l1 is None:
                curNode = l2
            else:
                curNode = l1

            curVal = curNode.val + c
            # TODO: pull into helper
            if curVal > 9:
                actualVal = curVal - 10
                carry = 1
            else:
                actualVal = curVal
                carry = 0        

            newNode = ListNode(actualVal)
            newNode.next = self.addTwoWithCarry(curNode.next, ListNode(0), carry)
            return newNode

        #neither l1 or l2 is defined
        elif c == 0:
            return None
        else:
            return ListNode(c)




class Solution:

    def addTwoNumbers(self, l1, l2):

        carry = 0
        head = None
        tail = None

        while True:

            # calc current val
            # both l1 and l2 are ListNodes
            if l1 is not None and l2 is not None:
                curVal = l1.val + l2.val + carry
                if curVal > 9:
                    curVal -= 10
                    carry = 1
                else:
                    carry = 0

            # both l1 and l2 are None
            elif l1 is None and l2 is None:
                if carry > 0:
                    curVal = carry
                    carry = 0
                else:
                    # l1 and l2 are None and carry=0
                    break

            # only l1 OR l2 is a ListNode
            else:
                if l1 is None:
                    l = l2
                else:
                    l = l1
                curVal = l.val + carry
                # TODO: refactor dupe logic???
                if curVal > 9:
                    curVal -= 10
                    carry = 1
                else:
                    carry = 0

            # increment all pointers
            #create node
            curNode = ListNode(curVal)

            if head is None:
                head = curNode
                tail = curNode
            else:
                tail.next = curNode
                tail = curNode

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return head


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

s = Solution()
a = s.addTwoNumbers(l1, l2)

print(repr(a))



l1 = ListNode(1)
l1.next = ListNode(8)
l2 = ListNode(0)
print(repr(s.addTwoNumbers(l1,l2)))
