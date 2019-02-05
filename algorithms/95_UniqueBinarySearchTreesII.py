r# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        if not n: return []
        l = [i+1 for i in range(n)]
        res = self.dfs(l)
        return res
    
    def dfs(self, remaining_arr):
        if not remaining_arr:
            return [None]
        
        trees = []
        for i in range(len(remaining_arr)):
            left_trees = self.dfs(remaining_arr[:i])
            right_trees = self.dfs(remaining_arr[i+1:])
            for l in left_trees:
                for r in right_trees:
                    root = TreeNode(remaining_arr[i])
                    root.left = l
                    root.right = r
                    trees.append(root)
        return trees