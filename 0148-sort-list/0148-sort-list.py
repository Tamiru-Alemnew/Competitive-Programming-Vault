# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        middle = self.getMiddle(head)
        left = head
        right = middle.next
        middle.next = None

        left = self.sortList(left)
        right = self.sortList(right)

        return self.merge(left, right)

    def getMiddle(self,head):
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, left, right ):
        dummy = ListNode(0)
        current = dummy
        while left and right:
            if left.val < right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next
        if left :current.next = left
        if right : current.next = right

        return dummy.next



