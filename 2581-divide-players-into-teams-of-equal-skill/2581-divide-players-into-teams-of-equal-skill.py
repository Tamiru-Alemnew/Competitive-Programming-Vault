class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        ans = 0 

        skill.sort()

        teamskill = skill[0] + skill[-1]
        l , r = 0 , len(skill) - 1

        while l < r :
            if skill[r] + skill[l] != teamskill:
                return -1

            ans += skill[r] * skill[l] 
            l += 1
            r -= 1

        return ans 

            
