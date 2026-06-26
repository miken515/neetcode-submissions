# Minimum Stack Solution
#
# This solution implements an efficient algorithm for the minimum stack problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        """Method: push"""
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        """Method: pop"""
        self.stack.pop()        
        self.minStack.pop()

    def top(self) -> int:
        """Method: top"""
        return self.stack[-1]

    def getMin(self) -> int:
        """Method: getMin"""
        return self.minStack[-1]
