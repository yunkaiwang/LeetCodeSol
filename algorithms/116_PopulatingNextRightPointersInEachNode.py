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
        if root.left != None and root.right != None:
            root.left.next = root.right
            self.connectLeftSubTree(root.left, root.right)
            self.connect(root.right)
        
    def connectLeftSubTree(self, root, firstRight):
        if root.left != None and root.right != None:
            root.left.next = root.right
            root.right.next = firstRight.left
            self.connectLeftSubTree(root.left, root.right)
            self.connectLeftSubTree(root.right, firstRight.left)
        else:
            root.next = firstRight
                
            
            
    
    