class MinStack:

    def __init__(self):
        self.stack = []
        self.min_vals = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_vals or val < self.getMin():
            self.min_vals.append(val)
        else:
            self.min_vals.append(self.getMin())

    def pop(self) -> None:
        self.stack = self.stack[:-1]
        self.min_vals = self.min_vals[:-1]
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_vals[-1]


