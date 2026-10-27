class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s):
            return ""

        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        window = {}
        have, required = 0, len(need)  # number of distinct chars whose count is satisfied
        res, res_len = (-1, -1), float("inf")
        l = 0

        for r, c in enumerate(s):
            window[c] = window.get(c, 0) + 1
            if c in need and window[c] == need[c]:
                have += 1

            # Window is valid: try to shrink it from the left
            while have == required:
                if r - l + 1 < res_len:
                    res, res_len = (l, r), r - l + 1

                left_char = s[l]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
                l += 1

        l, r = res
        return s[l : r + 1] if res_len != float("inf") else ""
