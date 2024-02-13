# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        ptr1 = head 
        ptr2 = head.next

        while ptr2:
            ptr1.val , ptr2.val = ptr2.val , ptr1.val
            if ptr2.next:
                ptr1 = ptr1.next.next
                ptr2 = ptr2.next.next
            else:
                break
        return head

