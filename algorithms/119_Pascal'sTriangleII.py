class Solution:
    def getRow(self, rowIndex: 'int') -> 'List[int]':
        """
        same implementation as the java version, but using python, the syntax is much easier to understand
        """
        lastList = [1]
        if rowIndex == 0: return lastList
        
        for i in range(1, rowIndex+1):
            lastList = [1] + [lastList[j-1] + lastList[j] for j in range(1, i)] + [1]
        return lastList
        