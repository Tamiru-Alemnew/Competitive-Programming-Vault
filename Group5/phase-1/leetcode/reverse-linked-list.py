# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dem = None
        current =head
        prev = None
        while current:
            dem= current.next
            current.next= prev 
            prev = current 
            current = dem 
        return prev 




        

