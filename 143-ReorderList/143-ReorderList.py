        second = slow.next 
        prev = slow.next = None
        while second:
            temp = second.next 
            second.next = prev
        slow , fast= head , head.next 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        
        """
        Do not return anything, modify head in-place instead.
        """
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
#         self.next = next
#         self.val = val
[
