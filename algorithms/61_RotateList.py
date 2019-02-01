# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        O(2 * n) = O(n) solution, much faster than recursive one, best runtime 40ms beats 100%. We need to traverse twice since the first traversal will tell us how many nodes are in the list, so that we can know much we need to rotate the list since k can be much larger than the length of the list but we can simply ignore those since when we rotate the list be its length, the list doesn't change, and for the second traversal, we need to keep track of the new head, which is denoted as c_p in the code, and the node whose next will be the original head, which is denoted as c in the node, ln is the new last node of the list whose next will be set to None.
        """
        if not (head and head.next):
            return head
        
        cur_p = head
        cur = head.next
        length = 2
        while cur.next:
            cur_p = cur
            cur = cur.next
            length += 1
            
        k = k % length
        if k == 0:
            return head
        
        ln = head
        c_p = ln.next
        c = head
        for _ in range(k):
            c = c.next
        
        while c.next:
            ln = ln.next
            c_p = ln.next
            c = c.next
        ln.next = None
        c.next = head
        return c_p
        


        """
        recursive solution, takes O(k%length * n) time, very inefficient, but it's still a solution (still beats 50% on Leetcode)
        """
        if k == 0:
            return head
        elif not (head and head.next):
            return head
        else:
            cur_p = head
            cur = head.next
            length = 2
            while cur.next:
                cur_p = cur
                cur = cur.next
                length += 1
            cur_p.next = None
            cur.next = head
            return self.rotateRight(cur, (k % length) - 1)