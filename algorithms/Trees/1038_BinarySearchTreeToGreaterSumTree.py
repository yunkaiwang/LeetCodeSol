# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.greaterSum = 0
        def helper(node):
            if not node:
                return
            helper(node.right)
            node.val, self.greaterSum = node.val + self.greaterSum, self.greaterSum + node.val
            helper(node.left)
        helper(root)
        return root