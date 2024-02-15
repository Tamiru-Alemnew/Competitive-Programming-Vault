class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        count = defaultdict(int)

        s = 0 
        cur = len(arr)
        mx = cur
        for a in arr:
            if a > len(arr) :
                s += 1
            count[a] += 1

        for i in range(len(arr)):
            
            if count[cur] == 0:
                if s > 0:
                    s -= 1
                else:
                    mx -=1
            elif count[cur] >1:
                s += count[cur] -1
            cur -= 1

        return mx
                
                

    
        

        

        
        



        