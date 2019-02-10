# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        
        current_level = [root]
        while current_level:
            queue = []
            for node in current_level:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            for i in range(len(queue) - 1):
                queue[i].next = queue[i+1]
            
            current_level = queue
            
        
   