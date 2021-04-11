"""
DFS

recursively find the LCA of the left child and the right child,
and also check the height of the two children, if their heights
are the same, then root is the LCA of the entire tree, otherwise
we return the corresponding LCA
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def helper(root: TreeNode) -> (TreeNode, int):
            if not root: return (None, 0)
            elif not root.left and not root.right: return (root, 1)
            n1, h1 = helper(root.left)
            n2, h2 = helper(root.right)
            if h1 == h2:
                return (root, 1+h1)
            elif h1 > h2:
                return (n1, 1+h1)
            else:
                return (n2, 1+h2)
        return helper(root)[0]