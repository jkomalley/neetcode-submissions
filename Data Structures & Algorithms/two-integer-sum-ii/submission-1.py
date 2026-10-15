class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num1 = 0
        num2 = len(numbers) - 1

        while (cur := numbers[num1] + numbers[num2]) != target:
            if cur < target:
                num1 += 1
            else:
                num2 -= 1

        return [num1 + 1, num2 + 1]
