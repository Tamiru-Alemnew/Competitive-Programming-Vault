class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        total = 2**(n-1)

        if n > 2:
            if k <= (total//2):
                return self.kthGrammar(n-1, k)
            else:
                if k > total//2 and k <= total*3/4:
                    return self.kthGrammar(n-1, k-total//4)
                else:
                    return self.kthGrammar(n-1, k-(3*total//4))
        elif n == 2:
            return 0 if k == 1 else 1
        else: 
            return 0