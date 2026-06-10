class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_sub = 0
        seen = set()
        start = 0
        end = 0
        while end < len(s):
            while s[end] in seen:
                seen.discard(s[start])
                start += 1
            seen.add(s[end])
            max_sub = max(max_sub, end - start + 1)
            end += 1

        return max_sub
            

"""
zxyzaxyz
s
 e

zx
"""