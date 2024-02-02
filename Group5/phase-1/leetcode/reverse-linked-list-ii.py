# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dem = None
        current = head
        prev = None
        left_node = head
        right_node = head
        left_prev = head
        
        if head.next and right > left:
            if left <= 1:
                left_prev = None
            else:
                for _ in range(left-2):
                    left_prev = left_prev.next 
            for _ in range(left-1):
                left_node = left_node.next 
            for _ in range(right-1):
                right_node = right_node.next
            right_side = right_node.next
            current = left_node.next
            prev = left_node
            
            for _ in range(right - left):      
                dem = current.next
                current.next = prev
                prev = current
                current = dem
            left_node.next = right_side
            if left_prev:
                left_prev.next = right_node
            else:
                head = right_node

        return head
