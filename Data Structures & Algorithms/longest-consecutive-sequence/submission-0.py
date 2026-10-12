class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        longest = 0

        for num in nums_set:
            if num - 1 in nums_set:
                continue

            cur = num
            while cur + 1 in nums_set:
                cur += 1

            longest = max(cur - num + 1, longest)

        return longest
