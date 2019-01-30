# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):

        """
        O(n) solution without using an extra variable as the previous node, runtime 48ms beats 55% (only slower than a bunch of people whose code runs in 44ms, but there is no difference)
        """
        dum = ListNode(-1)
        dum.next = head
        cur = dum
        while cur.next:
            if not cur.next.next:
                cur = cur.next
            elif cur.next.next and cur.next.val != cur.next.next.val:
                cur = cur.next
            else:
                while cur.next.next and cur.next.val == cur.next.next.val:
                    cur.next.next = cur.next.next.next
                cur.next = cur.next.next
        return dum.next
        