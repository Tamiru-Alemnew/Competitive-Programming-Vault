class MyStack:

    def __init__(self):
        self.stack = []
    def push(self, x: int) -> None:
    # append() function to push element in the stack
        self.stack.append(x)
    def pop(self) -> int:
    # pop() function to pop element from stack in LIFO order
        return self.stack.pop()
    def top(self) -> int:
        return self.stack[-1]
    def empty(self) -> bool:
        if len(self.stack) == 0:
            return True
        return False
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()