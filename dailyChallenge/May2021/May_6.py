# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head: return None
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        def listToBST(l):
            if not l: return None
            mid = len(l) // 2
            root = TreeNode(l[mid])
            root.left = listToBST(l[:mid])
            root.right = listToBST(l[mid + 1:])
            return root

        return listToBST(arr)
        # elif not head.next: return TreeNode(head.val)
        # prev, slow, fast = None, head, head
        # while fast and fast.next:
        #     fast = fast.next.next
        #     prev, slow = slow, slow.next
        # prev.next = None
        # root = TreeNode(slow.val)
        # root.left = self.sortedListToBST(head)
        # root.right = self.sortedListToBST(slow.next)
        # return root