class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        range_set = set()
        
        for r in ranges:
            for i in range(r[0], r[1] + 1):
                range_set.add(i)

        for i in range(left, right + 1):
            if i not in range_set:
                return False
                
        return True

