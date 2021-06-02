# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = curr = ListNode()
        carry = val = 0

        while carry or l1 or l2:
            val = carry

            if l1:
                l1, val = l1.next, l1.val + val
            if l2:
                l2, val = l2.next, l2.val + val

            carry, val = divmod(val, 10)
            curr.next = curr = ListNode(val)

        return head.next

l1 = ListNode(6,ListNode(3,ListNode(4,None)))
l2 = ListNode(8,ListNode(6,ListNode(4,None)))

sl = Solution()
l3 = sl.addTwoNumbers(l1,l2)

while l3:
    print(l3.val)

    l3=l3.next

