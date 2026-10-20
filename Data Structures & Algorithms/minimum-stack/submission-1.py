class MinStack:
    def __init__(self):
        self._stack = []
        self._min_stack = []

    def push(self, val: int) -> None:
        self._stack.append(val)
        self._min_stack.append(min(self._min_stack[-1] if len(self._min_stack) > 0 else val, val))

    def pop(self) -> None:
        self._min_stack.pop(-1)
        return self._stack.pop(-1)

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._min_stack[-1]
