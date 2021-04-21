class StackElement:
    def __init__(self, entry, smallest):
        self.entry = entry
        self.smallest = smallest


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        smallest = float('inf')
        if self.stack:
            smallest = self.stack[-1].smallest

        smallest = min(smallest, val)
        self.stack.append(StackElement(val, smallest))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1].entry
        return -1

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1].smallest
        return -1

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()