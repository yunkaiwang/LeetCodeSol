# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: 'TreeNode', x: 'int', y: 'int') -> 'bool':
        self.xlevel = None
        self.ylevel = None
        self.onSameTree = False
        self.findDepth(root, x, y, 0)
        if not self.onSameTree and self.xlevel == self.ylevel:
            return True
        return False
        
    def findDepth(self, root, x, y, currentDepth):
        if not root: return
        if not root.left and not root.right: return
        if not root.right:
            if root.left.val == x:
                self.xlevel = currentDepth + 1
            elif root.left.val == y:
                self.ylevel = currentDepth + 1
            else:
                self.findDepth(root.left, x, y, currentDepth + 1)
        elif not root.left:
            if root.right.val == x:
                self.xlevel = currentDepth + 1
            elif root.right.val == y:
                self.ylevel = currentDepth + 1
            else:
                self.findDepth(root.right, x, y, currentDepth + 1)
        else:
            if (root.left.val == x and root.right.val == y) or (root.right.val == x and root.left.val == x):
                self.onSameTree = True
            elif root.left.val == x or root.right.val == x:
                self.xlevel = currentDepth + 1
            elif root.right.val == y or root.left.val == y:
                self.ylevel = currentDepth + 1
            else:
                self.findDepth(root.left, x, y, currentDepth + 1)
                self.findDepth(root.right, x, y, currentDepth + 1)
        