# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy_node = ListNode(next=head)
      
        prefix_sums = {}
      
        current_sum, current_node = 0, dummy_node
        while current_node:
            current_sum += current_node.val
            prefix_sums[current_sum] = current_node
            current_node = current_node.next
      
        current_sum, current_node = 0, dummy_node
        while current_node:
            current_sum += current_node.val
            current_node.next = prefix_sums[current_sum].next
            current_node = current_node.next
      
        return dummy_node.next
        

            

            
        