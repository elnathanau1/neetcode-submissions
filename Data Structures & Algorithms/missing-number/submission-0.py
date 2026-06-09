class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0
        total_sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            total_sum += i
        
        total_sum += len(nums)
        return total_sum - sum