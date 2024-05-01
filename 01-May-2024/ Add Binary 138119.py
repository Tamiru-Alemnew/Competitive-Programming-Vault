# Problem:  Add Binary - https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            b = "0"*(len(a) - len(b)) + b
        else:
            a = "0"*(len(b) - len(a)) + a

        answer = []
        carry = 0
        for i in range(len(a)-1 , -1 ,-1):
            if carry > 0 :
                if a[i] == b[i]:
                    answer.append("1")
                    carry -= a[i] == "0"
                else:
                    answer.append("0")
            else:
                if a[i] != b[i]:
                    answer.append("1")
                else:
                    carry += a[i] == "1"
                    answer.append("0")

        while carry > 0:
            answer.append("1")
            carry -= 1

        answer.reverse()

        return "".join(answer)

            




        
        