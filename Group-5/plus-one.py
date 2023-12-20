class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits=list(map(str, digits))
        ans="".join(digits)
        r = int(ans) +1
        a = str(r)
        fi=[char for char in a]
        fi=list(map(int,fi))
        return fi