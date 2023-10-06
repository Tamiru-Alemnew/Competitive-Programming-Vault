# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy= ListNode(0,head)
        prev,cur=head,head.next
        while cur:
            if cur.val >prev.val:
                prev,cur=cur,cur.next
                continue
            pointer = dummy
            while cur.val>pointer.next.val:
                pointer=pointer.next
            prev.next = cur.next
            cur.next=pointer.next
            pointer.next=cur
            cur=prev.next
        return dummy.next