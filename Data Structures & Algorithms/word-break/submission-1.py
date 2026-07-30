class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        possible = [False] * len(s)
        for word in wordDict:
            if s[:len(word)] == word:
                possible[len(word) - 1] = True
        for i in range(len(possible)):
            if possible[i]:
                for word in wordDict:
                    if i + len(word) < len(s) and s[i + 1:i + len(word) + 1] == word:
                        possible[i + len(word)] = True

        return possible[-1]

"""
n e e t c o d e 
f f f t f f f f

"""
        # wordSet = set(wordDict)
        # found = False
        # def dfs(startIndex: int):
        #     nonlocal found
        #     if startIndex == len(s):
        #         found = True
        #         return 
        #     for word in wordSet:
        #         if found: 
        #             return
        #         if startIndex + len(word) > len(s):
        #             continue
        #         if word == s[startIndex:startIndex + len(word)]:
        #             dfs(startIndex + len(word))
        
        # dfs(0)
        # return found