"""
Swapping Nodes in a Linked List

Description: You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth
node from the beginning and the kth node from the end (the list is 1-indexed).

Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]

Solution: Not much to say, simple solution using O(1) space and running in
O(n) time. Only traverse the linkedlist once and doesn't turn the linkedlist
into an array
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        kThFromHead = head

        for _ in range(k - 1):
            if kThFromHead.next:
                kThFromHead = kThFromHead.next
            else:  # there are less than k elements in the list, nothing to swap
                return head

        kThFromTail, curr = head, kThFromHead

        while curr.next:
            kThFromTail = kThFromTail.next
            curr = curr.next

        kThFromHead.val, kThFromTail.val = kThFromTail.val, kThFromHead.val

        return head
