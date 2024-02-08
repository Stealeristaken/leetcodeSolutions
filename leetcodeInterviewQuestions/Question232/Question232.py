class MyQueue:

    def __init__(self):
        self.idx = 0
        self.size = 10
        self.stack = []
        self.infinity_stack = []

    def push(self, x: int) -> None:
        if len(self.stack) >= self.size:
            self.infinity_stack.append(x)
        else:
            self.stack.append(x)

    def pop(self) -> int:
        item = self.stack[self.idx]
        self.idx += 1
        if self.idx >= len(self.stack):
            self.stack = self.infinity_stack
            self.infinity_stack = []
            self.idx = 0
        return item

    def peek(self) -> int:
        return self.stack[self.idx]

    def empty(self) -> bool:
        return len(self.stack) == 0 and len(self.infinity_stack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()