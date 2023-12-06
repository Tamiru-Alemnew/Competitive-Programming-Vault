class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ones = []

        for i in range(len(boxes)):
            if boxes[i]=="1":
                ones.append(i)

        ans = []
        for i in range(len(boxes)):
            temp = 0
            for index in ones:
                temp += abs(index- i)
            ans.append(temp)
        return ans 


