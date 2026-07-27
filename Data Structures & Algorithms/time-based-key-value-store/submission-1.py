class TimeMap:

    def __init__(self):
        self.storage = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storage.keys():
            self.storage[key] = []
        self.storage[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.storage.keys():
            return ""
        
        timestamps = self.storage[key]
        if timestamp < timestamps[0][0]: 
            return ""
        elif timestamp >= timestamps[-1][0]:
            return timestamps[-1][1]
        
        low = 0
        high = len(timestamps)
        while low < high:
            mid = (low + high) // 2
            mid_timestamp = timestamps[mid]
            if timestamp >= mid_timestamp[0] and timestamp < timestamps[mid + 1][0]:
                return mid_timestamp[1]
            elif timestamp < mid_timestamp[0]:
                high = mid
            else:
                low = mid + 1
            
        return ""

"""
test -> 
10, one
20, two
30, three
"""
