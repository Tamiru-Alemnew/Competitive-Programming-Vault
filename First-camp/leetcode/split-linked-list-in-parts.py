# Definition for singly-linked list.
# class ListNode:
#     def init(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        node = head
        while node:
            n += 1
            node = node.next

        place = n // k
        rem = n % k
        ans = []
        part = [0]*k
        for i in range(k):
            part[i] += place
            part[i] += rem >= 1
            rem -= 1

        dummy = head
        for p in part:
           
            temp = dummy
           
            for i in range(p-1):
                if not dummy:
                    break
                dummy = dummy.next

            if dummy:
                tempNode = dummy.next
                dummy.next = None
                dummy = tempNode
            else:
                dummy = None 
            ans.append(temp)


        return ans