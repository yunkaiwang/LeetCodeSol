
class Solution:
    def isValidBST(self, root, upper_limit=None, lower_limit=None):
        """
        iterative approach using inorder traversal
        """
        stack = []
        prev = -float('inf')
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right
        return True
            

        """
        recursive solution
        """
        if not root:
            return True
        if upper_limit != None and root.val >= upper_limit:
            return False
        elif lower_limit != None and root.val <= lower_limit:
            return False
        
        return self.isValidBST(root.left, upper_limit = root.val, lower_limit=lower_limit) and self.isValidBST(root.right, upper_limit=upper_limit, lower_limit = root.val)
        
        