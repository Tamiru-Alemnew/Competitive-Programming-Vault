class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def rev(s , l , r):
            if l < r :
                s[l] , s[r] = s[r] ,s[l] 
                rev(s,l+1 , r-1)
            
        rev(s , 0 , len(s)-1)

        