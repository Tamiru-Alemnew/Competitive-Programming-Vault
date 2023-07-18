class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indx={}
        for i,char  in enumerate(nums):
            comp = target - char 
            if comp in indx :
                return [indx[comp],i]
            indx[char] = i 
        return none