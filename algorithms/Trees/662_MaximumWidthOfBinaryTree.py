# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        levelMinMax = [[0, 0]]

        def levelOrder(root, currentLevel, levelStr):
            if not root: return
            if currentLevel > len(levelMinMax):
                levelMinMax.append([int(levelStr, 2), int(levelStr, 2)])

            i = int(levelStr, 2)
            if i < levelMinMax[currentLevel - 1][0]:
                levelMinMax[currentLevel - 1][0] = i
            elif i > levelMinMax[currentLevel - 1][1]:
                levelMinMax[currentLevel - 1][1] = i

            levelOrder(root.left, currentLevel + 1, levelStr + '0')
            levelOrder(root.right, currentLevel + 1, levelStr + '1')

        levelOrder(root.left, 2, '0')
        levelOrder(root.right, 2, '1')
        return max([m2 - m1 + 1 for m1, m2 in levelMinMax])