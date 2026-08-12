class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counts = {}
        for c in list(s):
            counts[c] = counts.get(c, 0) + 1
        ret_list = []

        count = 0
        seen = set()
        for i in range(len(s)):
            c = s[i]
            counts[c] -= 1
            count += 1
            if counts[c] != 0:
                seen.add(c)
            else:
                if c in seen:
                    seen.remove(c)
            if not seen:
                ret_list.append(count)
                count = 0
        if count != 0:
            ret_list.append(count)
        return ret_list