class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastOccurrence={}
        for i, c in enumerate(s):
            lastOccurrence[c]=i
        partition =[]
        size , end = 0 , 0
        for i ,c in enumerate(s):
            size += 1
            end=max(end, lastOccurrence[c])
            if i == end:
                partition.append(size)
                size = 0

        return partition 
        