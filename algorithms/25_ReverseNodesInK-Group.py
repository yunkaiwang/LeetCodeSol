# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        O(n) solution with O(1) extra space, best run time is 80ms beats 94%
        """
        if not head or not head.next:
            return head
        
        dummyHead = ListNode(-1)
        cur_node = dummyHead
        dummyHead.next = head
        
        while cur_node:
            temp = cur_node
            for _ in range(k): # go k step far to see if we reached the end or not
                temp = temp.next
                if not temp:
                    return dummyHead.next
            
            temp_next = temp.next
            
            temp.next = cur_node.next
            cur_node.next = temp
            cur_node = temp
            temp = temp.next
            
            for _ in range(k - 2):
                next_two = temp.next
                temp.next = next_two.next
                next_two.next = cur_node.next
                cur_node.next = next_two
            
            temp.next = temp_next
            cur_node = temp
            
        return dummyHead.next