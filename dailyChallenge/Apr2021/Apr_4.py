"""
Design Circular Queue

Nothing particular about the question, use a simple array
and keep track of the start and end position
"""
class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.queue = [-1] * k
        self.start, self.end = 0, -1
        self.curSize = 0

    def enQueue(self, value: int) -> bool:
        if self.curSize >= self.size:
            return False

        self.end = (self.end + 1) % self.size
        self.queue[self.end] = value
        self.curSize += 1

        return True

    def deQueue(self) -> bool:
        if self.curSize <= 0:
            return False
        self.curSize -= 1
        self.start = (self.start + 1) % self.size
        return True

    def Front(self) -> int:
        if self.curSize <= 0:
            return -1
        return self.queue[self.start]

    def Rear(self) -> int:
        if self.curSize <= 0:
            return -1
        return self.queue[self.end]

    def isEmpty(self) -> bool:
        return self.curSize == 0

    def isFull(self) -> bool:
        return self.curSize == self.size

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()