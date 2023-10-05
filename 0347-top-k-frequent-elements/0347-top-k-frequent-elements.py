class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict(sorted(Counter(nums).items(), key = lambda item : item[1]))
        ans = []
        l = len(count.items())
        k = l - k
        while k < l:
            temp = count.popitem()
            ans.append(temp[0])
            k+=1
        return ans


