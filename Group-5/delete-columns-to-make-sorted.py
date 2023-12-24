class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        strs = list(zip(*strs))
        y = 0 
        for s in strs:
            c = sorted(s)
            print(c , s)
            for i in range(len(s)):
                if c[i] != s[i]:
                    y += 1
                    break 

        return y
        