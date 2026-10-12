class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []

        ret = [1] * len(nums)

        prefix = 1
        suffix = 1

        for i in range(len(nums)):
            ret[i] *= prefix
            ret[-1 - i] *= suffix
            prefix *= nums[i]
            suffix *= nums[-1 - i]

        return ret
