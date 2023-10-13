class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = { c : i for i,c in enumerate(s)}

        end =  size = 0 
        ans = []
        for i , c in enumerate(s):
            size += 1
            end = max(lastIndex[c], end)
            if i == end:
                ans.append(size)
                size = 0 
        return ans 
                