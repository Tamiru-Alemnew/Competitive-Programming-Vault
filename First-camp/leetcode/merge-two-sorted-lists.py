# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val < list2.val:
            cur = list1
            after = self.mergeTwoLists(list1.next , list2)
            cur.next = after
        else:
            cur = list2
            after = self.mergeTwoLists(list1 , list2.next)
            cur.next = after

        return cur

        