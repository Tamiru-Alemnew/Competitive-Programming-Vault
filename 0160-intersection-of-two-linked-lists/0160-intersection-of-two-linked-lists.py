# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen = set()
        dummy = ListNode()
        dummy.next = headA

        while dummy :
            seen.add(dummy.next)
            dummy = dummy.next

        dumm = ListNode()
        dumm.next = headB

        while dumm:
            if dumm.next in seen:
                return dumm.next
            
            dumm = dumm.next
        
        return None
            


            
        
        

        
        