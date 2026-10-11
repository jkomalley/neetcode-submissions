from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]

        for value, count in counts.items():
            buckets[count].append(value)
        
        result = []
        for values in buckets[::-1]:
            for value in values:
                result.append(value)
                if len(result) == k:
                    return result
