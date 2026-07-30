class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def isPeak(index: int) -> boolean:
            left = float('-inf') if index - 1 < 0 else nums[index - 1]
            right = float('-inf') if index + 1 >= len(nums) else nums[index + 1]
            if nums[index] > left and nums[index] > right:
                return 0
            if nums[index] > left and right > nums[index]:
                return 1
            else:
                return -1
        
        start = 0
        end = len(nums)
        while start < end:
            mid = (end + start) // 2
            foundPeak = isPeak(mid)
            if foundPeak == 0:
                return mid
            elif foundPeak > 0:
                start = mid + 1
            else:
                end = mid
        return -1


"""
1. peak 
2. Going up
3. Going down


1 2 1 3 4 5 0
|
            |
"""