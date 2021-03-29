# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: 'TreeNode', x: 'int', y: 'int') -> 'bool':
        if not root or root.val == x or root.val == y: return False
        queue = [root]
        found = False
        parent = None
        while queue:
            next_queue = []
            for node in queue:
                if node.left:
                    if node.left.val == x or node.left.val == y:
                        if found:
                            return True
                        parent = node
                        found = True
                    else:
                        next_queue.append(node.left)
                if node.right:
                    if node.right.val == x or node.right.val == y:
                        if found:
                            return not node == parent
                        parent = node
                        found = True
                    else:
                        next_queue.append(node.right)
            if found:
                return False
            else:
                queue = next_queue
        return False
        