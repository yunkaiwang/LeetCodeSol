# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: 'TreeNode') -> 'int':
        """
        construct the number from top to bottom, very simple question, runtime is 36ms beats 100%
        """
        self.sum = 0
        self.sumNumbersHelper(root, 0)
        return self.sum
        
    def sumNumbersHelper(self, node, cur_sum):
        if node == None:
            return
        
        cur_sum *= 10
        cur_sum += node.val
        if node.left != None or node.right != None:
            self.sumNumbersHelper(node.left, cur_sum)
            self.sumNumbersHelper(node.right, cur_sum)
        else:
            self.sum += cur_sum