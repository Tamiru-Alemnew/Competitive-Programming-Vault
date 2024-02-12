class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0 
        cur = head
        while cur:
            length += 1
            if length == k:
                first = cur
            cur = cur.next

        second = head
        for _ in range(length - k):
            second = second.next

        first.val, second.val = second.val, first.val

        return head
