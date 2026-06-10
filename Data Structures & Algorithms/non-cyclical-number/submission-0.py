class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            temp_sum = 0
            for char in str(n):
                temp_sum += int(char) ** 2
            n = temp_sum
        return n == 1

