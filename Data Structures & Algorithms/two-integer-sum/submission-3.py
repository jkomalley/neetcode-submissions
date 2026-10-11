class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            diff = target - num

            try:
                j = nums.index(diff, i+1)
            except ValueError:
                continue
            else:
                return [i, j]