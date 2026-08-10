class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        count_map = {}
        for i in hand:
            count_map[i] = count_map.get(i, 0) + 1
        
        for i in hand:
            if count_map[i] == 0:
                continue
            for j in range(groupSize):
                if i + j not in count_map.keys() or count_map[i + j] == 0:
                    return False
                count_map[i + j] -= 1
            
        return True
"""
1 2 2 3 3 4 4 5

1 2 3 4
2 3 4 5

"""