# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x = ListNode()
        c = x
        cr = 0
        while l1 or l2 or cr:
            y = cr
            if l1:
                y += l1.val
                l1 = l1.next
            if l2:
                y += l2.val
                l2 = l2.next
            cr, y = divmod(y, 10)
            c.next = ListNode(y)
            c = c.next
        return x.next