# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy = ListNode(-1, head)
        prev, curr = dummy, head
        while curr and curr.val < x:
            prev, curr = curr, curr.next

        # there does not exist a node in the list that has value >= x
        if not curr: return head
        nHead = curr
        nPrev = prev
        while curr:
            if curr.val < x:
                temp = curr.next
                prev.next, prev = curr, curr
                nPrev.next = curr.next
                curr.next, curr = nHead, temp
                curr = temp
            else:
                nPrev, curr = curr, curr.next
        return dummy.next
