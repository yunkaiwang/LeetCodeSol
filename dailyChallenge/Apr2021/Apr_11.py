"""
Deepest Leaves Sum

Level order traversal, O(n) time O(n) space
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root: return 0
        queue = [root]
        leafSum = 0
        while queue:
            leafSum = 0
            nextQueue = []
            while queue:
                root = queue.pop()
                leafSum += root.val
                if root.left:
                    nextQueue.append(root.left)
                if root.right:
                    nextQueue.append(root.right)
            queue = nextQueue
        return leafSum