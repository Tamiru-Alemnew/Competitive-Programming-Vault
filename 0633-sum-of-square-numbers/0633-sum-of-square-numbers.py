class Solution:
    def judgeSquareSum(self, c: int) -> bool:
      
        left, right = 0, int(c**(1/2))
        while left<=right:
            sum = right**2 + left**2
            if sum == c:
                return True 
            if sum < c:
                left+=1
            else:
                right -=1
        return False
        