# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head: return head
        p1, p1_prev, p2 = head, None, head
        for _ in range(n):
            p2 = p2.next
        
        while p2:
            p1_prev = p1
            p1 = p1.next
            p2 = p2.next
        
        if p1_prev:
            p1_prev.next = p1.next
        else: # if the head is the node that need to be removed
            head = p1.next
        
        return head