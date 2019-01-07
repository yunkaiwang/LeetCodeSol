# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    """
    This problem is very straight forward, improvement is still possible, but they are all O(n) approaches
    """
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        cds = l1.val + l2.val # current digit sum
        sum_head = ListNode(cds%10)
        extra = cds//10
        currentNode = sum_head
        l1 = l1.next
        l2 = l2.next
        
        while not l1 == None or not l2 == None:
            val1 = l1.val if not l1==None else 0
            val2 = l2.val if not l2==None else 0
            cds =  val1 + val2 + extra
            
            currentNode.next = ListNode(cds%10)
            extra = cds//10
            currentNode = currentNode.next
            
            if not l1 == None:
                l1 = l1.next
            if not l2 == None:
                l2 = l2.next
            
        if extra:
            currentNode.next = ListNode(extra)
        
        return sum_head
            
            
            