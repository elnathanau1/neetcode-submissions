class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total_sum = 0
        for i in range(len(nums)):
            total_sum -= nums[i]
            total_sum += i
        
        total_sum += len(nums)
        return total_sum