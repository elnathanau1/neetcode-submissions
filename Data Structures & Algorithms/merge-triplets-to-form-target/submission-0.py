class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        complete = [False, False, False]
        for x,y,z in triplets: 
            if x <= target[0] and y <= target[1] and z <= target[2]:
                if x == target[0]:
                    complete[0] = True
                if y == target[1]:
                    complete[1] = True
                if z == target[2]:
                    complete[2] = True
        return complete[0] and complete[1] and complete[2]
"""
(2,5,6), (1,4,4), (5,7,5) -> (5,4,6)

5 -> 2
4 -> 1


"""