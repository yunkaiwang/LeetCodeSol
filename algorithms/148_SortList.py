# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        cur = slow.next
        slow.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(cur)
        return self.merge(l1, l2)
    
    def merge(self, l1, l2):
        dummy = ListNode(-1)
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
                cur = cur.next
            else:
                cur.next = l2
                l2 = l2.next
                cur = cur.next
        cur.next = l1 if l1 else l2
        return dummy.next