class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {} # hash of character set, list of strings
        for string in strs:
            char_list = [0] * 26
            for c in string:
                index = ord(c) - ord('a')
                char_list[index] += 1
            key = str(char_list)
            if key in anagram_map:
                anagram_map[key].append(string)
            else:
                anagram_map[key] = [string]
        return list(anagram_map.values())
