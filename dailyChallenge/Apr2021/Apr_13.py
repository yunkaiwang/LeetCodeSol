"""
Flatten Nested List Iterator
"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.flatternList = []
        stack = nestedList[::-1]
        while stack:
            nestInt = stack.pop()
            while nestInt and not nestInt.isInteger():
                l = nestInt.getList()
                if l:
                    nestInt = l[0]
                    for i in range(len(l) - 1, 0, -1):
                        stack.append(l[i])
                else:
                    nestInt = stack.pop() if stack else None

            if nestInt:
                self.flatternList.append(nestInt.getInteger())
        self.flatternList = self.flatternList[::-1]

    def next(self) -> int:
        if not self.hasNext(): return -1
        return self.flatternList.pop()

    def hasNext(self) -> bool:
        return len(self.flatternList) > 0

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())