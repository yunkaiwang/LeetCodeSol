# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        Use two pointers to loop through the list once, running time is O(n), best run 60ms, beats 98%
        """
        
        pre_node = None
        remove_node = head
        cur_node = head
        count = 1
        while count < n:
            cur_node = cur_node.next
            count += 1
        
        if cur_node.next == None:
            head = remove_node.next
            return head
        
        while cur_node.next != None:
            pre_node = remove_node
            cur_node = cur_node.next
            remove_node = remove_node.next
            
        pre_node.next = remove_node.next
        return head