# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.head = head 
        count = 0 
        locate=self.head 
        middle = self.head 
        while not locate== None:
            count +=1
            locate=locate.next 
        mid = count//2
        for i in range(mid):
            middle = middle.next
            
          
        return middle 