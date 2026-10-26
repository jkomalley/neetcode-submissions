class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False

        c1 = [0] * 26
        c2 = [0] * 26
        for i in range(n):
            c1[ord(s1[i]) - ord("a")] += 1
            c2[ord(s2[i]) - ord("a")] += 1

        matches = sum(1 for i in range(26) if c1[i] == c2[i])

        for r in range(n, m):
            if matches == 26:
                return True

            # Add the new character on the right
            idx = ord(s2[r]) - ord("a")
            c2[idx] += 1
            if c2[idx] == c1[idx]:
                matches += 1
            elif c2[idx] == c1[idx] + 1:
                matches -= 1

            # Remove the old character on the left
            idx = ord(s2[r - n]) - ord("a")
            c2[idx] -= 1
            if c2[idx] == c1[idx]:
                matches += 1
            elif c2[idx] == c1[idx] - 1:
                matches -= 1

        return matches == 26
