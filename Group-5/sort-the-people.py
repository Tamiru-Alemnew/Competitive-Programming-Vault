class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)

        for i in range(n):
            max_ind = i 

            for j in range(i+1 , n):
                if heights[max_ind] < heights[j]:
                    max_ind = j

            names[max_ind] , names[i] = names[i] , names[max_ind]
            heights[max_ind] , heights[i] = heights[i] , heights[max_ind]
        return names
