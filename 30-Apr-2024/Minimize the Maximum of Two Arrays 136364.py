# Problem: Minimize the Maximum of Two Arrays - https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/

class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:

        l , r = 0 , 10**10

        def check(num):
            missing1 = num // divisor1
            missing2  = num // divisor2
            missing3 = num // math.lcm(divisor1 , divisor2 )

            return num -  missing3 >=  uniqueCnt1 +  uniqueCnt2 and num - missing2 >=  uniqueCnt2 and num - missing1 >=  uniqueCnt1

        while l < r :
            md = ( l + r ) // 2 
            
            if check(md):
                r = md 
            else:
                l = md + 1

        return l
        

        

