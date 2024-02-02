# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Check for special cases
        if not head or n <= 0:
            return head

        # Calculate the length of the linked list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        #  where n is greater than or equal to the length
        if n >= length:
            return head.next

        #the node to be removed
        to_be_removed = head
        for _ in range(length - n - 1):
            to_be_removed = to_be_removed.next

        # Remove the node by adjusting pointers
        to_be_removed.next = to_be_removed.next.next

        return head

        

