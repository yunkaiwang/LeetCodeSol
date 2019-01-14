# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from Queue import PriorityQueue

class Solution(object):
    def mergeKLists(self, lists):
        """
        Two solutions provided, one runs in O(N log k) where N is the total number of nodes and k is the number of lists, the best runtime is 180ms, this should be the fastest way of solving this problem, however, my second solution, which is putting everything into a list and then sort it, then create a ListNode for each value, this one should runs in O(N logN) time, but when I tried on LeetCode, the best runtime is 84ms which is much faster than the first solution, I am guessing it because I used Python list.sort() method which is already optimized to run in shorter time whenever possible.
        """
        pqueue = PriorityQueue()
        for l in lists:
            if l:
                pqueue.put((l.val, l))
        
        head = ListNode(-1)
        cur_node = head
        while not pqueue.empty():
            val, node = pqueue.get()
            cur_node.next = node
            cur_node = node
            node = node.next
            if node:
                pqueue.put((node.val, node))
        return head.next

        """
        start of solution 2 using sort
        """
        # list = []
        # for l in lists:
        #     while l:
        #         list.append(l.val)
        #         l = l.next
        
        # list.sort()
        # head = cur = ListNode(-1)
        # for val in list:
        #     cur.next = ListNode(val)
        #     cur = cur.next
        # return head.next