class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_counts = {}
        for num in nums:
            if num_counts.get(num):
                return True
            num_counts[num] = True
        return False