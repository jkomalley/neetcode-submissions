class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ret = 0
        n = len(heights)
        i = 0
        j = n - 1

        while i != j:
            cur = (j - i) * min(heights[i], heights[j])
            ret = max(cur, ret)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return ret
