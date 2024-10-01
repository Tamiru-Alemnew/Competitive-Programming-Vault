from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, arr: List[int]) -> int:
        min_subs = []
        for n in arr:
            ind = bisect_left(min_subs , n)

            if ind == len(min_subs):
                min_subs.append(n)
            else:
                min_subs[ind] = n 

        return len(min_subs)


