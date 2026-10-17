class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix_maxs = []
        postfix_maxs = []
        cur_max = 0

        for i in range(n):
            prefix_maxs.append(cur_max)
            cur_max = max(cur_max, height[i])

        cur_max = 0
        for i in range(n - 1, -1, -1):
            postfix_maxs.append(cur_max)
            cur_max = max(cur_max, height[i])

        postfix_maxs.reverse()

        ret = 0
        for i in range(n):
            ret += max(0, min(prefix_maxs[i], postfix_maxs[i]) - height[i])

        return ret
