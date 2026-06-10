class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        def bs(start: int, end: int, target: int) -> int:
            while start <= end:
                mid = (start + end) // 2
                if numbers[mid] == target:
                    return mid
                elif numbers[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
            return -1

        for i in range(len(numbers) - 2):
            maybe_found = bs(i + 1, len(numbers) - 1, target - numbers[i])
            if maybe_found != -1:
                return [1 + i, 1 + maybe_found]
        
        if numbers[len(numbers) - 2] + numbers[len(numbers) - 1] == target:
            return [len(numbers) - 1, len(numbers)]
        
        return []
        


"""
1 2 3 4
s
      e
"""