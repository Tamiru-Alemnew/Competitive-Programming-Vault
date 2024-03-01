class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
   
        third_value = float('-inf')
   
        stack = []
     
        for number in reversed(nums):

            if number < third_value:
                return True

            while stack and stack[-1] < number:
                third_value = stack.pop()

            stack.append(number)

        return False