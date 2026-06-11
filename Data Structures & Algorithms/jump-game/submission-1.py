class Solution:
    def canJump(self, nums: List[int]) -> bool:
        nums.reverse()

        can_reach_list = [True]
        for i in range(1, len(nums)):
            can_reach = False
            for j in range(1, nums[i] + 1):
                can_reach = can_reach or can_reach_list[i - j]
            can_reach_list.append(can_reach)
        
        return can_reach_list[-1]


"""

0 0 2
T F 
i = 1
cr = F
j = 1

"""