# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        O(m + n) solution where m is length of l1 and n is length of l2, create a dummy node with -1 as value simply save us from checking if head is none every time, as with this dummy node, we can simply set the cur_node next every time.
        Best runtime 64ms, beats 99%
        """
        if not l1: return l2
        if not l2: return l1
        
        head = ListNode(-1)
        cur_node = head
        while l1 and l2:
            v1 = l1.val
            v2 = l2.val
            
            if v1 < v2:
                cur_node.next = l1
                l1 = l1.next
            else:
                cur_node.next = l2
                l2 = l2.next
            cur_node = cur_node.next
        
        if l1:
            cur_node.next = l1
        else:
            cur_node.next = l2
        return head.next
                
        