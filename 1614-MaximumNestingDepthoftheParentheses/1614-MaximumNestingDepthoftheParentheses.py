class Solution:
    def maxDepth(self, s: str) -> int:
        stack  = []
        depth = 0 
        for char in s:
            if char == "(":
                stack.append(char)
                depth = max(depth , len(stack))
            elif char == ")":
                stack.pop()

        return depth 
"
