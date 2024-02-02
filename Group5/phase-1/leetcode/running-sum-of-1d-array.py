class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        temp = 0 
        sum =[]
        for num in nums:
            temp += num
            sum.append(temp)
        return sum