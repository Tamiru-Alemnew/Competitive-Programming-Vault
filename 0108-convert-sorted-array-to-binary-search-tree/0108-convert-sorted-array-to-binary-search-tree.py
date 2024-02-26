# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def help(nums):
            if len(nums) <= 0:
                return  
                
            mid = len(nums) //2 

            node = TreeNode(nums[mid])
            node.left = help(nums[:mid])
            node.right = help(nums[mid+1:])


            return node

        return help(nums)

          

        