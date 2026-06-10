class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        max_area = 0

        while start < end:
            dist = end - start
            max_area = max(min(heights[start], heights[end]) * dist, max_area)
            if heights[start] > heights[end]:
                end -= 1
            else:
                start += 1
        
        return max_area

"""
1 7 2 5 4 7 3 6
  s
          e

dist = 6
max_water = (min start, end) * dist = 6 * 6 = 36

while start < end:
    dist = end - start
    if start_height > end_height:
        end --
    else start ++


"""