# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        arr = []

        stack = [(root, 0)]
        while stack:
            node, depth = stack.pop()
            if len(arr) <= depth:
                arr.append(node.val)
            elif arr[depth] < node.val:
                arr[depth] = node.val

            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))

        return arr
