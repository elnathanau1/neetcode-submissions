class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        ret_list = []
        temp = []

        used_interval = False
        index = 0

        def chooseNext() -> List[int]:
            nonlocal index
            nonlocal used_interval
            if index >= len(intervals):
                used_interval = True
                return newInterval
            elif used_interval:
                index += 1
                return intervals[index - 1]
            elif intervals[index][0] <= newInterval[0]:
                index += 1
                return intervals[index - 1]
            else:
                used_interval = True
                return newInterval

        while index < len(intervals) or not used_interval:
            interval = chooseNext().copy()
            if not temp:
                temp = interval
            
            elif interval[0] > temp[1]:
                ret_list.append(temp.copy())
                temp = interval

            else:
                temp[1] = max(interval[1], temp[1])

        
        if temp:
            ret_list.append(temp.copy())

        return ret_list

            
"""
intervals = [[1,2],[3,5],[9,10]], newInterval = [5,7]

ret = [[1,2]]
temp = [3,5]

"""