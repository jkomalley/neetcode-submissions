class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = [0] * len(temperatures)
        stack = []

        for i, cur in reversed(list(enumerate(temperatures))):
            while stack and stack[-1][1] <= cur:
                stack.pop()

            ret[i] = stack[-1][0] - i if stack else 0

            stack.append((i, cur))

        return ret
