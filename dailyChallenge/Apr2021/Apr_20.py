"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        stack = [root]
        order = []
        while stack:
            node = stack.pop()
            order.append(node.val)
            stack += node.children[::-1] if node.children else []
        return order