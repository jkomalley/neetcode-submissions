from itertools import combinations


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        ret = set()

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1

            while j != k:
                if -nums[i] == nums[j] + nums[k]:
                    ret.add((nums[i], nums[j], nums[k]))
                    j += 1
                elif -nums[i] < nums[j] + nums[k]:
                    k -= 1
                else:
                    j += 1

        return [list(i) for i in ret]
