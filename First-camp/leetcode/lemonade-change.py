class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        stored = defaultdict(int)
        for b in bills:
            stored[b] += 1
            
            if b == 20:
                if stored[10] >= 1:
                    stored[10] -= 1
                    if stored[5] > 0 :
                        stored[5] -= 1
                    else:
                        return False
                else:
                    if stored[5] >= 3:
                        stored[5] -= 3
                    else:
                        return False

            elif b == 10 :
                if stored[5] >=1:
                    stored[5] -= 1
                else:
                    return False
        return True

                    

            
 
        