# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy = ListNode(0 , list1)
        s = dummy
        e = dummy 
        for i in range(a):
            s = s.next

        for j in range(b + 1):
            e = e.next

        temp = list2

        while temp.next:
            temp = temp.next

        s.next = list2
        temp.next = e.next

        return dummy.next

