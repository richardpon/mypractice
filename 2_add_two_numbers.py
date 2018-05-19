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


class Solution:

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



l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

s = Solution()
a = s.addTwoNumbers(l1, l2)

print("A")
print(str(a))
print(repr(a))
        
            

        