import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        smallest_seen = max(piles)

        def hoursNeeded(k: int) -> int:
            h = 0
            for pile in piles:
                h += math.ceil(pile / k)
            return h

        def bs(start: int, end: int):
            if start > end:
                return 
            
            mid = (start + end) // 2
            mid_val = hoursNeeded(mid)
            nonlocal smallest_seen

            if mid_val <= h:
                smallest_seen = min(smallest_seen, mid)
                bs(start, mid - 1)
            else:
                bs(mid + 1, end)
        
        bs(1, max(piles))
        return smallest_seen