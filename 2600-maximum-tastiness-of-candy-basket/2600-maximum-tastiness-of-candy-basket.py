class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        def check(x):
            last , count, i = price[0], 1, 1
            while count < k and i < len(price):
                if price[i] - last >= x :
                    last , count = price[i], count + 1
                i +=1
            return count == k 

        l, h = 0 , price[len(price)-1]

        while l < h:
            mid = (l + h )//2
            if check(mid):
                l = mid+1
            else:
                h = mid 
        return l - 1