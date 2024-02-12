class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = Counter(blocks[:k])
        min_rec = count ["W"]
        rec =  count ["W"]
        
        for i in range(k,len(blocks)):
            rec += blocks[i] =="W"
            rec -= blocks[i-k] == "W"
            min_rec = min(min_rec , rec)

        return min_rec

