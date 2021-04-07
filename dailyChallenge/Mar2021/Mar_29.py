# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        self.arr = []
        self.index = 0
        self.canFlip = True

        def dfs(node):
            if not node or not self.canFlip:
                return

            if node.val != voyage[self.index]:
                self.canFlip = False
                return
            self.index += 1
            if node.left and node.right and node.right.val == voyage[self.index]:
                self.arr.append(node.val)
                dfs(node.right)
                dfs(node.left)
            else:
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return self.arr if self.canFlip else [-1]



