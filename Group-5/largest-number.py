class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        num = [str(i) for i in nums]
        num.sort(  key=LargerNumKey)
        return "0" if num[0] == "0" else "".join(num) 


        
        