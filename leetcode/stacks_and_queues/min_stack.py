class MinStack:

    def __init__(self):
        self.stack = []
        # Track min values as they are pushed and popped
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        # Only append the stack's first item and 
        # subsequent elements <= min's last item
        if len(self.stack) == 1:
            self.min.append(val)
        elif val <= self.min[-1]:
            self.min.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()

        # Pop from min if the stack's pop is in min's last item
        if popped == self.min[-1]:
            self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()