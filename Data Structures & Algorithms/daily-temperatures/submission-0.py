class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            index = len(temperatures) - i - 1
            if len(stack) == 0:
                result[index] = 0
            
            for j in range(len(stack)):
                temp, future_index = stack[len(stack) - j - 1]
                if temp > temperatures[index]:
                    result[index] = future_index - index
                    break

            while stack and stack[-1][0] < temperatures[index]:
                stack.pop()
            stack.append((temperatures[index], index))

        return result
        
"""
30 38 30 36 35 40 28
1  4  1  2  1  0  0


top  36 40 bottom

"""