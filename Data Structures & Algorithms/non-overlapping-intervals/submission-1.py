class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        temp = intervals[0]
        eraseCount = 0
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] < temp[1]:
                eraseCount += 1
                temp[1] = min(temp[1], interval[1])
            else:
                temp = interval
        return eraseCount
        
"""
[[1,2],[2,4],[1,4]]

"""