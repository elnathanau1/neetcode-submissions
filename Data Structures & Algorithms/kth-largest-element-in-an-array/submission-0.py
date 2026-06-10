import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def partition(nums: List[int]) -> (List[int], List[int], List[int]):
            curr = nums[random.randint(0, len(nums) - 1)]

            less = []
            greater = []
            equal = []
            for num in nums:
                if num < curr:
                    less.append(num)
                elif num > curr:
                    greater.append(num)
                else:
                    equal.append(num)
            return (less, greater, equal) 

        while True:
            lesser, greater, equal = partition(nums)
            if len(greater) == k - 1: 
                return equal[0]
            elif len(greater) > k - 1:
                nums = greater
            elif len(greater) < k - 1 and len(greater) + len(equal) > k-1:
                return equal[0]
            else:
                nums = lesser
                k -= len(greater) + len(equal)
                
