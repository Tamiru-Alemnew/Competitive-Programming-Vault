class ATM:

    def __init__(self):
        self.atm = [0 , 0 , 0 , 0 ,0]
        self.note = {0:20 ,1 :50 , 2:100 , 3:200 , 4:500 }   

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.atm[i] += banknotesCount[i]     
    def withdraw(self, amount: int) -> List[int]:
        ans =[0 , 0 , 0 , 0 ,0]
        for i in range(4,-1,-1):
            count = self.atm[i]
            note = self.note[i]
            minus = min(amount//note,count )
            if minus:
                amount -= minus*note
                ans[i] += minus  
        if amount: 
            return [-1]
        for i in range(5):
            self.atm[i] -= ans[i]
        return ans
        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)