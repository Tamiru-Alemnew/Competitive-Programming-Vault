class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        minimum_add = 0
        current_open = 0 


        for bracket in s:
            if current_open and bracket == ")" :
                current_open -= 1
                minimum_add -= 1
            else:

                current_open += bracket == "("
                minimum_add += 1

        return minimum_add