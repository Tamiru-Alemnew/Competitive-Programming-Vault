class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        l = 0 
        r = len(letters)
        ans = letters[0]
        while l < r :
            mid = (l + r ) // 2 
            if letters[mid] > target:
                r = mid
                ans = letters[mid]
            else:
                l = mid + 1

        return ans



        
        