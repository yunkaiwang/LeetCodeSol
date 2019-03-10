class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        # O(n) solution using stack
        root = TreeNode(preorder[0])
        s = [root]
        for i in range(1, len(preorder)):
            a = None
            while len(s) != 0 and preorder[i] > s[-1].val:
                a = s.pop()
            if a != None:
                a.right = TreeNode(preorder[i])
                s.append(a.right)
            else:
                s[-1].left = TreeNode(preorder[i])
                s.append(s[-1].left)
        return root

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        # O(n^2) solution using recursive traversal
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        i = 1
        while i < len(preorder):
            if preorder[i] > root.val:
                break
            i+=1
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root