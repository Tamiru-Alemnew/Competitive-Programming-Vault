class Solution:
    def interpret(self, command: str) -> str:
        obj = { "G":"G" ,"()":'o',"(al)":"al" }
        ans =''
        temp = ""
        for char in command:
            temp += char
            if temp in obj :
                 ans += obj[temp]
                 temp =""
        return ans