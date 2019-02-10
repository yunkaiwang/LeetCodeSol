# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        self.sol = -float('inf')
        self.max(root)
        return self.sol
    
    def max(self, root):
        if not root: return 0
        left = self.max(root.left)
        right = self.max(root.right)
        self.sol = max(max(left, 0) + max(right, 0) + root.val, self.sol)
        return max(root.val, max(left, right) + root.val)
        
        