class Solution:
    def checkValidString(self, s: str) -> bool:
        open_balance = 0 

        for char in s:
            if char in '(*':
                open_balance += 1
            elif open_balance:
                open_balance -= 1 
            else:
                return False

        closed_balance = 0 

        for char in s[::-1]:
            if char in '*)':
                closed_balance += 1 
            elif closed_balance:
                closed_balance -= 1 
            else:
                return False

        return True
