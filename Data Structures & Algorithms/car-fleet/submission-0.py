class Node:
    def __init__(self, position: int, speed: int):
        self.position = position
        self.speed = speed
        self.next = None

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []
        for i in range(len(position)):
            fleets.append((position[i], speed[i]))

        fleets.sort()
        
        time_to_dest = [(target - x[0]) / x[1] for x in fleets]

        stack = []
        for time in time_to_dest:
            while stack and stack[-1] <= time:
                stack.pop()
            stack.append(time)
        return len(stack)            
            

"""
2 2 1 1
4 1 0 7  -  10

1  2  2  1
0  1  4  7
10 9  6  3
10 5  3  3

10 5 3

"""