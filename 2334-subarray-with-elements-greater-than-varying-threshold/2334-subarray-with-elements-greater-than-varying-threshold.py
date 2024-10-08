class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        
        smallest = nums[0]
        temp_leng = math.ceil((threshold + 1 )// nums[0])
        current_leng = 1
        ans = -1
        
        for n in nums[1:]:
            if temp_leng > len(nums) or n < smallest :
                if current_leng >= temp_leng:
                    ans = max(ans , current_leng)

                temp_leng = math.ceil((threshold + 1 )// n)
                current_leng = 1
                smallest = n 
            else:
                current_leng += 1

        if current_leng >= temp_leng:
             ans = max(ans , current_leng)


        return ans

            



        


