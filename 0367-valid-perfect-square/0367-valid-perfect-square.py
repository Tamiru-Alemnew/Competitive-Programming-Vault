class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l , r = 0 , num

        while r >= l:
            mid = l + (r-l) //2

            if mid*mid == num:
                return True
            elif mid*mid > num:
                r = mid-1
            else:
                l = mid +1

        return False
