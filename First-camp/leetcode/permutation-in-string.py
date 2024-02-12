class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        s2_count = Counter(s2[:len(s1)])
        if s1_count == s2_count:
            return True
        for i in range(len(s1),len(s2)):
            
            s2_count[s2[i]] =s2_count.get(s2[i] , 0) + 1
            s2_count[s2[i-len(s1)]] -= 1

            if s1_count == s2_count:
                return True
            
        return False
        

        
        