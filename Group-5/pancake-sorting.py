class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(sublist, k ):
            x = 0 
            while x < k/2:
                sublist[x], sublist[k-1-x] = sublist[k-1-x], sublist[x] 
                x +=1

        res = []
        current = len(arr)
        while current:
            idx = arr.index(current)

            if idx != current -1:
                if idx != 0:
                    res.append(idx + 1)
                    flip(arr, idx + 1)
                res.append(current)
                flip(arr, current)
            current -= 1
        return res

