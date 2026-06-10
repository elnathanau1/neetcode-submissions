class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums) * 2
        while len(nums) < length:
            nums.append(nums[len(nums) - length // 2])
        return nums