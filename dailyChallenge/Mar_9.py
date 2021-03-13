"""
Add One Row to Tree

Given the root of a binary tree and two integers val and depth,
add a row of nodes with value val at the given depth depth.

Note that the root node is at depth 1.

The adding rule is:
- Given the integer depth, for each not null tree node cur at the depth depth - 1,
  create two tree nodes with value val as cur's left subtree root and right subtree root.
- cur's original left subtree should be the left subtree of the new left subtree root.
- cur's original right subtree should be the right subtree of the new right subtree root.
- If depth == 1 that means there is no depth depth - 1 at all, then create a tree node with
  value val as the new root of the whole original tree, and the original tree is the new root's
  left subtree.

Input: root = [4,2,6,3,1,5], val = 1, depth = 2
Output: [4,1,1,2,null,null,6,3,1,5]

Solution: Not much to say, traditional dfs can solve the problem easily.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def addOneRow(self, root, val, depth):
        def addRow(root, val, depth, current_depth):
            if root == None:
                return
            if current_depth < depth - 1:
                addRow(root.left, val, depth, current_depth + 1)
                addRow(root.right, val, depth, current_depth + 1)
            else:
                newLeftNode, newRightNode = TreeNode(val), TreeNode(val)
                newLeftNode.left = root.left
                newRightNode.right = root.right
                root.left = newLeftNode
                root.right = newRightNode

        if depth == 1:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot

        addRow(root, val, depth, 1)
        return root