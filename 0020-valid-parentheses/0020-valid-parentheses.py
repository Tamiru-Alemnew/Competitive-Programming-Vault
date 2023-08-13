class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = "([{"
        match = {"]": "[", "}": "{", ")": "("}
        stack = []
        
        for char in s:
            if char in open_brackets:
                stack.append(char)
            else:
                if stack and match[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
