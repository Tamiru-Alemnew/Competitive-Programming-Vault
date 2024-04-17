# Problem: Find K Closest Elements - https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        temp = []
        for i in range(len(arr)):
            temp.append((abs(x - arr[i]) ,arr[i]))

        heapify(temp)
        candidates = []
        
        for i in range(k):
            distance , val = heappop(temp)
            candidates.append(val)

        result = []
        heapify(candidates)
        for i in range(len(candidates)):
            result.append(heappop(candidates))


        return result

        



        