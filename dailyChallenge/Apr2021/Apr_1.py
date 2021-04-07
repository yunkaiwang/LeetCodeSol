"""
Palindrome Linked List

O(n) time solution with O(1) space
- find the middle node
- reverse the second half of the linked list
- compare the first half with the reversed second half
- return false if any pair of nodes don't match
- we can reverse the second half back if we want to (not done in the solution listed here)

Two reverse functions provided:
- one is iterative reverse, O(1) space
- the other one is recursive reverse, O(n) space (O(1) if we don't consider function call stack as extra space)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next

        fast = head
        slow = self.reverse(slow)
        while slow:
            if slow.val != fast.val:
                return False
            slow = slow.next
            fast = fast.next
        return True

    # iterative reverse
    def reverse(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev

    # recursive reverse
    def reverse2(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head

        nhead = self.reverse2(head.next)
        head.next.next = head
        head.next = None
        return nhead