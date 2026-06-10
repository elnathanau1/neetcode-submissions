class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_link = 0
        num_set = set(nums)
        while num_set:
            i = num_set.pop()
            count = 1
            temp = i
            while temp + 1 in num_set:
                count += 1
                num_set.remove(temp + 1)
                temp += 1
            temp = i
            while temp - 1 in num_set:
                count += 1
                num_set.remove(temp - 1)
                temp -= 1

            max_link = max(max_link, count)    

        return max_link