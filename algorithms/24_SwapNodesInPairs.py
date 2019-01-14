# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        nothing to say about this one, simple check if next two pointers are empty, if not then swap them (not swaping the values!), O(n) solution provided, best run time 52ms beats 99.5%
        """
        if not head or not head.next:
            return head
        
        node = head.next
        head.next = node.next
        node.next = head
        head = node
        
        node = node.next
        while node.next and node.next.next:
            next_node = node.next
            next_2_node = node.next.next
            
            next_node.next = next_2_node.next
            next_2_node.next = next_node
            node.next = next_2_node
            node = node.next.next
        return head