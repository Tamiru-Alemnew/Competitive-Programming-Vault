class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            for j in range( i + 1 , len(nums) - 2 ):
                l , r = j + 1 , len(nums) -1

                while l < r :
                    if nums[i] + nums[j] + nums[l] + nums[r] == target:
                        if [nums[i] , nums[j] , nums[l] , nums[r]] not in ans:
                            ans.append([nums[i] , nums[j] , nums[l] , nums[r]])
                        l += 1
                        r -= 1
                         
                    elif nums[i] + nums[j] + nums[l] + nums[r] < target:
                        l += 1
                    else:
                        r -= 1
        return ans 
                
                        