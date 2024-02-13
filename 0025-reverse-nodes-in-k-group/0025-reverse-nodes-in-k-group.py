class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0 
        cur = head 

        while cur :
            length += 1
            cur = cur.next

        rem  = length % k
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        cur = head
        j = 0 
    
        while j < length - rem:
            cur = prev_group_end.next
            for i in range(k-1):
                next_node = cur.next
                cur.next = next_node.next
                next_node.next = prev_group_end.next
                prev_group_end.next = next_node

            prev_group_end = cur
            j += k

        return dummy.next