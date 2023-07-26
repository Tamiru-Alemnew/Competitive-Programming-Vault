class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ps, cnt, curr_sum = [0], 0, 0

        for num in nums:
            curr_sum += num
            ps.append(curr_sum)

        sums_count = {}
        for i in range(len(ps)):
            if ps[i] - k in sums_count:
                cnt += sums_count[ps[i] - k]

            sums_count[ps[i]] = sums_count.get(ps[i], 0) + 1

        return cnt
