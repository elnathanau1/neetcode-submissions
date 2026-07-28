class Solution:
    def findMin(self, nums: List[int]) -> int:
        # properly sorted, can just return first value
        if nums[0] <= nums[-1]:
            return nums[0]
        # has a pivot
        start = nums[0]
        end = nums[-1]
        mid = nums[len(nums) // 2]
        if mid < nums[len(nums) // 2 - 1]:
            return mid
        if start < mid: 
            return self.findMin(nums[len(nums) // 2 :])
        else:
            return self.findMin(nums[: len(nums) // 2])


"""
minimum is going to either be: 
1. all the way on the left
2. less than the value on the left

normally sorted s-m, so go m-e
3 4 5 6 1 2
s = 3
m = 6
e = 2

pivot between s-m, normal m-e, so s-m
6 1 2
s = 6
m = 1
e = 2


4 5 0 1 2 3
s 4
m 1
e 3


"""