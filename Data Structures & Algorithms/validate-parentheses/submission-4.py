class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'}
        stack = []
        for char in s:
            if char in pairs:
                if not stack or pairs[char] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)
        if stack:
            return False
        return True
