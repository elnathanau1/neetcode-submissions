class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        max_distance = nums[0]
        jumps = 1
        index = 0
        while max_distance < len(nums) - 1:
            jump_distance = max_distance
            while index < jump_distance:
                index += 1
                max_distance = max(index + nums[index], max_distance)
            jumps += 1
        return jumps


        
"""
2 4 1 1 1 1 

len(nums) - 1 = 5
max_dist = 2
jumps = 1
index = 1
jump_dist = 2

"""