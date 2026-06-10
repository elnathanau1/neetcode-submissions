class Solution:
    def isValid(self, s: str) -> bool:
        push_set = set(['(', '{', '['])
        stack = []
        for char in s:
            if char in push_set:
                stack.append(char)
            elif not stack:
                return False
            elif char == ')':
                if stack.pop() != '(':
                    return False
            elif char == ']':
                if stack.pop() != '[':
                    return False
            elif char == '}':
                if stack.pop() != '{':
                    return False
        return len(stack) == 0
            