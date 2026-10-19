from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        par_open_to_closed = {"(": ")", "{": "}", "[": "]"}
        par_open = par_open_to_closed.keys()
        par_closed = par_open_to_closed.values()

        for ch in s:
            if ch in par_open:
                stack.append(ch)
            elif ch in par_closed:
                if len(stack) == 0 or par_open_to_closed[stack.pop()] != ch:
                    return False

        return len(stack) == 0
