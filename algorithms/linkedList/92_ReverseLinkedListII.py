# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        if not head or left == right:
            return head

        cur, prev = head, None

        while left > 1:
            cur, prev = cur.next, cur
            left -= 1
            right -= 1

        tail, con = cur, prev

        while right:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            right -= 1

        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur
        return head
