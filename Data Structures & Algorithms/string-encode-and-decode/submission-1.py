class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_strs = [f"{len(x)},{x}" for x in strs]
        return "".join(encoded_strs)

    def decode(self, s: str) -> List[str]:
        ret_list = []

        start = 0
        end = 0

        while start < len(s):
            while end < len(s) and s[end] != ',':
                end += 1
            length = int(s[start:end])
            start = end + 1
            end = start + length
            ret_list.append(s[start:end])
            start = end
            end = start
        return ret_list

"""
5,Hello5,World
  s
       e
"""
    