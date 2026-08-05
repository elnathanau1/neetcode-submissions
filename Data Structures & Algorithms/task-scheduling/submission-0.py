from collections import deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}
        for task in tasks:
            counts[task] = counts.get(task, 0) + 1
        heap = []
        for _, count in counts.items():
            heapq.heappush(heap, -count)

        queue = deque()
        time = 0
        while queue or heap:
            time += 1
            if heap:
                temp_count = heapq.heappop(heap)
                temp_count += 1
                if temp_count != 0:
                    queue.append((temp_count, time + n))
            while queue and queue[0][1] <= time:
                heapq.heappush(heap, queue.popleft()[0])
            
        return time



"""
X X Y Y
X Y  X Y

A A A B C n = 3
A B C i A i i A

"""