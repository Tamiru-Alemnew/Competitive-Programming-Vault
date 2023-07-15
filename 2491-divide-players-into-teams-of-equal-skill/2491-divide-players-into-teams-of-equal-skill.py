class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        total = sum(skill) 
        Nteam = len(skill)//2
        if total % Nteam != 0:
            return -1
        TeamSkill = total // Nteam
        skill.sort()
        left,right,chemistry = 0 , len(skill)-1,0
        while right >= left:
            if skill[left] + skill[right]!= TeamSkill:
                return -1
            chemistry += skill[left]*skill[right]
            left +=1
            right -=1
        return chemistry 