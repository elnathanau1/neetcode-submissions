class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret_list = []
        index_map = {}
        for i, num in enumerate(nums):
            if num in index_map:
                index_map[num].add(i)
            else:
                index_map[num] = set()
                index_map[num].add(i)
        
        seen = set()
        for i, num in enumerate(nums[:len(nums) - 1]):
            index_map[num].discard(i)
            for j in range(i + 1, len(nums)):
                temp_target = -1 * (nums[i] + nums[j])
                if temp_target in index_map:
                    for k in index_map[temp_target]:
                        if k != i and k != j:
                            seen_key = [nums[i], nums[j], nums[k]]
                            seen_key.sort()
                            if (seen_key[0], seen_key[1], seen_key[2]) not in seen: 
                                ret_list.append([nums[i],nums[j],nums[k]])
                                seen.add((seen_key[0], seen_key[1], seen_key[2]))
        
        return ret_list
