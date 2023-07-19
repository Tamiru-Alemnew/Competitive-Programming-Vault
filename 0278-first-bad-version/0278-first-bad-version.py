# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        arr=range(1,n,1)
        left , right = 1, n
        while right > left:
            mid= left + (right - left) // 2
            x= isBadVersion(mid)
            if x :
                right = mid
                    
            else:
                left = mid + 1
        return right