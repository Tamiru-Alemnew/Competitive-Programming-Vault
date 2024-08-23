class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        first = 0 
        second = 0 
        ans = []

        while first < len(firstList) and second < len(secondList):
            a = max(firstList[first][0] , secondList[second][0])
            b = min(firstList[first][1] , secondList[second][1]) 

            if b == firstList[first][1] :
                first += 1

            if b == secondList[second][1]:
                second += 1
            if b >= a :
                ans.append([a , b])
        return ans 

