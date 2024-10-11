class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()

        """
        1 2 3 4 5 6 7 8 
        !       !
          !       !
            !       ! 
              !       !

              
        """
        if len(nums) <= 4:
            return 0 
            
        return min(nums[-4] - nums[0],
                    nums[-3] - nums[1] , 
                    nums[-2] - nums[2],
                    nums[-1] - nums[3])