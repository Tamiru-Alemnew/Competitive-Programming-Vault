class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ind_sum={}
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    ind_sum[list1[i]] = i+j
        lst=[]
        for i,j in ind_sum.items():
            if j == min(ind_sum.values()):
                lst.append(i)
        return lst