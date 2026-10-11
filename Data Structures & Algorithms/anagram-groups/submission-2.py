from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            groups[frozenset(Counter(s).items())].append(s)
        
        return list(groups.values())
