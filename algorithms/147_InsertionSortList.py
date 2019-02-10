# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: 'ListNode') -> 'ListNode':
        """
        keep a sorted list and always add new element to the corresponding position
        """
        if not head:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        remaining_list = head.next
        head.next = None
        while remaining_list:
            prev = dummy
            cur = dummy.next
            while cur and cur.val < remaining_list.val:
                prev = cur
                cur = cur.next
            
            temp = remaining_list.next
            remaining_list.next = prev.next
            prev.next = remaining_list
            remaining_list = temp
        
        return dummy.next
                
                