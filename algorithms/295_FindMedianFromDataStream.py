import bisect 

class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
    
    def balance(self):
        if len(self.left) >= len(self.right) + 2:
            self.right = [self.left[-1]] + self.right
            self.left = self.left[:-1]
        elif len(self.right) >= len(self.left) + 2:
            self.left = self.left + [self.right[0]]
            self.right = self.right[1:]

    def addNum(self, num: int) -> None:
        if not self.left:
            self.left = [num]
        elif num <= self.left[-1]:
            bisect.insort(self.left, num)
        else:
            bisect.insort(self.right, num)
        self.balance()
        

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (self.left[-1] + self.right[0]) / 2
        else:
            return self.left[-1] if len(self.left) > len(self.right) else self.right[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()