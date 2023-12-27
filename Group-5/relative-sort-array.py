class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ind = {}
        for i in range(len(arr2)):
            ind[arr2[i]] = i 
        def custome(num):
            if num not in ind:
                return num + len(arr2)
            return ind[num]

        arr1.sort(key = custome)

        return arr1



