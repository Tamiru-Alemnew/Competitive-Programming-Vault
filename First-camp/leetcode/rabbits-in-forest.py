class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = defaultdict(int)
        ans = 0 
        for n in answers:
            if count[n] == 0 :
                ans += n +1
                count[n] = n 
            else:
                count[n] -= 1

        return ans 
        