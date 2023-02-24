class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        elif self.minStack[-1] >= val:
            self.minStack.append(val)

    def pop(self) -> None:
        if self.minStack and self.stack[-1] == self.minStack[-1]:
            self.minStack.pop()
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()