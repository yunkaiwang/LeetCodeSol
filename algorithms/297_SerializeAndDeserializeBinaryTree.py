# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        if not root:
            return "#"
        else:
            return str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)
        

    def deserialize(self, data):
        self.index = 0
        nodes = data.split(",")
        def helper():
            if nodes[self.index] == "#":
                self.index+=1
                return None
            root = TreeNode(int(nodes[self.index]))
            self.index += 1
            root.left = helper()
            root.right = helper()
            return root
        return helper()
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))