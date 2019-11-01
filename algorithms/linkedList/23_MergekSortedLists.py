# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from Queue import PriorityQueue

class Solution(object):
    def mergeKLists(self, lists):
        """
        This solution runs in O(N log k) where N is the total number of nodes and k is the number of lists, the best runtime is 180ms, this should be the fastest way of solving this problem, however, my second solution, which is putting everything into a list and then sort it, then create a ListNode for each value, this one should runs in O(N logN) time, but when I tried on LeetCode, the best runtime is 84ms which is much faster than the first solution, I am guessing it because I used Python list.sort() method which is already optimized to run in shorter time whenever possible.
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
    This solution uses merge two lists function that was implemented in question #21 as a helper function. The run time is also O(nlogk), the idea is recursively combine two lists until there is only one list left. The analyzation of this question is very similar to the analyzation of mergesort. At each level, you will do O(n) work, and there will be at most O(logk) levels, so the total run time is O(nlogk).
    """
    """
    def mergeKLists(self, lists):
        def mergeTwoLists(l1, l2):
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
        
        while len(lists) > 1:
            new_lists = []
            for i in range(0, len(lists)-1, 2):
                new_lists.append(mergeTwoLists(lists[i], lists[i+1]))
            if len(lists) % 2:
                new_lists.append(lists[-1])
            lists = new_lists
        return lists[0] if lists else None
    """
                
        