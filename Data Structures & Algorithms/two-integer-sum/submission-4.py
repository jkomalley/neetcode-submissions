class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            if (diff := target - num) in seen:
                return [seen[diff], i]
            seen[num] = i