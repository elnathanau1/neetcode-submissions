import heapq
class MedianFinder:

    def __init__(self):
        self.bottom_half = []
        self.top_half = []

    def addNum(self, num: int) -> None:
        if not self.bottom_half and not self.top_half:
            self.top_half.append(num)
        elif num >= self.top_half[0]:
            heapq.heappush(self.top_half, num)
            self.rebalance()
        else:
            heapq.heappush(self.bottom_half, num * -1)
            self.rebalance()

    def findMedian(self) -> float:
        if not self.bottom_half:
            return self.top_half[0]
        elif not self.top_half:
            return -1 * self.bottom_half[0]
        elif len(self.bottom_half) > len(self.top_half):
            return -1 * self.bottom_half[0]
        elif len(self.bottom_half) < len(self.top_half):
            return self.top_half[0]
        else:
            return (self.top_half[0] + -1 * self.bottom_half[0]) / 2
        
        
    def rebalance(self):
        while abs(len(self.top_half) - len(self.bottom_half)) > 1:
            if len(self.top_half) > len(self.bottom_half) + 1:
                heapq.heappush(self.bottom_half, -1 * heapq.heappop(self.top_half))
            elif len(self.bottom_half) > len(self.top_half) + 1:
                heapq.heappush(self.top_half, -1 * heapq.heappop(self.bottom_half))


"""
bottom
-5

top


"""