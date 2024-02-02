# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd, even = ListNode(0,head),  ListNode(0,head)
        otail, etail , length = odd, even, 1
        if not head or not head.next:
            return head
        while head:
            if length % 2 == 0:
                etail.next = head 
                etail = head
            else:
                otail.next = head 
                otail = head
            length += 1 
            head = head.next
        otail.next = even.next
        etail.next = None
        return odd.next