# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def findLeaves(root):
            if not root: return []
            elif not root.left and not root.right: return [root.val]
            else: return findLeaves(root.left) + findLeaves(root.right)
        return findLeaves(root1) == findLeaves(root2)