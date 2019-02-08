# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    O(n^2) solution, inefficient, but very easy to think of
    """
    def buildTree(self, preorder: 'List[int]', inorder: 'List[int]') -> 'TreeNode':
        self.preorder = preorder
        root = self.buildTreeHelper(inorder)
        return root
        
    def buildTreeHelper(self, inorder):
        if not inorder:
            return None
        
        root = TreeNode(self.preorder[0])
        i = inorder.index(self.preorder[0])
        self.preorder = self.preorder[1:]
        
        root.left = self.buildTreeHelper(inorder[:i])
        root.right = self.buildTreeHelper(inorder[i+1:])
        return root


    """
    O(n) solution, use a hashmap to simply the effort for searching
    """
    def buildTree(self, preorder: 'List[int]', inorder: 'List[int]') -> 'TreeNode':
        self.pre_index = 0
        dict = {}
        for i, num in enumerate(inorder):
            dict[num] = i
        
        def helper(in_left, in_right):
            if in_left > in_right:
                return None
            
            root_val = preorder[self.pre_index]
            root = TreeNode(root_val)
            self.pre_index += 1
            
            root.left = helper(in_left, dict[root_val] - 1)
            root.right = helper(dict[root_val] + 1, in_right)
            return root
        
        return helper(0, len(inorder) - 1)