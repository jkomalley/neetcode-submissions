class Solution:
    def isPalindrome(self, s: str) -> bool:
        _s = ("".join([c for c in s if c.isalnum()])).lower()
        if len(_s) == 1: return True
        return _s[: len(_s) // 2 + len(_s) % 2] == _s[: len(_s) // 2 - 1 : -1]
