class Solution:
    def compress(self, chars: List[str]) -> int:
        l = res = 0 

        while l < len(chars):
            grpLeng = 1 

            while(grpLeng + l < len(chars) and chars[l] == chars[grpLeng + l]):
                grpLeng += 1

            chars[res] = chars[l]
            res += 1 
            
            if grpLeng > 1 :
                temp = str(grpLeng)
                chars[res: res + len(temp)] = list(temp)
                res += len(temp)
            l += grpLeng

        return res

        