# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        curNode, head = None, None
        
        addOne = False
        while l1 and l2:
            s = l1.val + l2.val
            if addOne:
                s = s + 1
                addOne = False
            if s > 9:
                addOne = True
                s = s - 10
            
            if head:
                curNode.next = ListNode(s)
                curNode = curNode.next
            else:
                curNode = ListNode(s)
                head = curNode
            
            l1 = l1.next
            l2 = l2.next
        
        while l1 or l2:
            s = l1.val if l1 else l2.val
            if addOne:
                s = s + 1
                addOne = False
            if s > 9:
                addOne = True
                s = s - 10
            curNode.next = ListNode(s)
            curNode = curNode.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if addOne:
            curNode.next = ListNode(1)
        
        return head