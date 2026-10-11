class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            angrm = "".join(sorted(s))
            groups[angrm] = groups.get(angrm, []) + [s]
        
        return list(groups.values())
        
