class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        for c in s:
            counts[c] = counts.get(c, 0) + 1
        for t in t:
            if t not in counts:
                return False
            counts[t] = counts[t] - 1
            if counts[t] == 0:
                del counts[t]
        return not counts