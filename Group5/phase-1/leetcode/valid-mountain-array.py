class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        max_val = max(arr)

        if arr[0] == max_val or arr[-1] == max_val:
            return False
        else:
            prev = arr[0]
            flag = False

            for i in range(1,len(arr)):
                if arr[i] == max_val and not flag:
                    flag = True
                elif not flag and (arr[i] >= max_val or arr[i] <= prev):
                    return False
                elif flag and (arr[i] >= max_val or arr[i] >= prev):
                    return False

                prev = arr[i]
            return True