class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        visited  , ans = set() , set()

        for l in range(len(s) - 9):
            cur = s[l: l + 10]

            if cur in visited:
                ans.add(cur)
            visited.add(cur)
        return list(ans)