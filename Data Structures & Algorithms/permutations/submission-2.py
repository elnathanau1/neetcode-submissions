import copy

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        ret_list = []
        for i in range(len(nums)):
            temp = self.permute(nums[:i] + nums[i + 1:])
            for possible in temp:
                ret_list.append([nums[i]] + possible)
        return ret_list





'''
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
'''