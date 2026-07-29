class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        ret_list = []
        temp = []
        for interval in intervals:
            if not temp: 
                temp = interval.copy()
            elif interval[0] > temp[1]:
                ret_list.append(temp.copy())
                temp = interval.copy()
            else:
                temp[1] = max(temp[1], interval[1])
        
        if temp:
            ret_list.append(temp)
        return ret_list