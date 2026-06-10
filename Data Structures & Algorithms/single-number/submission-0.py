class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor_sum = nums[0]
        for num in nums[1:]:
            xor_sum = xor_sum ^ num
        return xor_sum