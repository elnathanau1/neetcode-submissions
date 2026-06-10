class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        post = [1] * len(nums)
        for i in range(1, len(nums)):
            pre[i] *= nums[i - 1] * pre[i - 1]
            j = len(nums) - i - 1
            post[j] *= nums[j + 1] * post[j + 1]
        
        ret = [1] * len(nums)
        for i in range(len(nums)):
            ret[i] *= pre[i] * post[i]
        return ret