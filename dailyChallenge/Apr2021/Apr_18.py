# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1, head)
        curr = head
        while n:
            curr = curr.next
            n -= 1

        prev = dummy
        while curr:
            curr = curr.next
            prev = prev.next

        prev.next = prev.next.next
        return dummy.next