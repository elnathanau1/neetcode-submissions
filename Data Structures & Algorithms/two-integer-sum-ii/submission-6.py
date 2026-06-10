class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        sum = numbers[start] + numbers[end]
        while sum != target:
            if target > sum:
                start += 1
            else:
                end -= 1
            sum = numbers[start] + numbers[end]
        return [start + 1, end + 1]




"""
-8 -3 0 2 4 10 target -1
s
e
temp 2
"""