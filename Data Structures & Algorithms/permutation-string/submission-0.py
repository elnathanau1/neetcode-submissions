class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): 
            return False

        s1_counts = [0] * 26
        s2_counts = [0] * 26

        def compare() -> bool:
            for i in range(26):
                if s1_counts[i] != s2_counts[i]:
                    return False
            return True

        for i in range(len(s1)):
            s1_index, s2_index = ord(s1[i]) - ord('a'), ord(s2[i]) - ord('a')
            s1_counts[s1_index] += 1
            s2_counts[s2_index] += 1
        
        if compare():
            return True
        
        start = 0
        end = len(s1) - 1
        while end < len(s2) - 1:
            end += 1
            s2_counts[ord(s2[end]) - ord('a')] += 1
            s2_counts[ord(s2[start]) - ord('a')] -= 1
            start += 1
            if compare():
                return True
        
        return False