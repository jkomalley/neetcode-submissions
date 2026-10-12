class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []

        ret = [1] * len(nums)

        prefix = 1

        for i, num in enumerate(nums):
            ret[i] *= prefix
            prefix *= num

        suffix = 1
        for i, num in enumerate(nums[::-1]):
            ret[-1 - i] *= suffix
            suffix *= num

        return ret
