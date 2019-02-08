# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: 'List[int]', postorder: 'List[int]') -> 'TreeNode':
        """
        O(n) space and O(n) time        
        """
        self.post_index = len(postorder) - 1
        dict = {}
        for i, num in enumerate(inorder):
            dict[num] = i
        
        def helper(in_left, in_right):
            if in_left > in_right:
                return None
            
            root_val = postorder[self.post_index]
            root = TreeNode(root_val)
            self.post_index -= 1
            if in_left < in_right:
                root.right = helper(dict[root_val] + 1, in_right)
                root.left = helper(in_left, dict[root_val] - 1)
            return root
        
        return helper(0, len(inorder) - 1)