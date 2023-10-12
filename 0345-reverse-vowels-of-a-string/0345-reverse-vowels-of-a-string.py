class Solution:
    def reverseVowels(self, s: str) -> str:
        l , r = 0 , len(s) -1 
        vowels = 'aeiouAEIOU'
        s = list(s)
        while l < r:
            if s[l] in vowels and s[r] in vowels:
                s[l] , s[r] = s[r] , s[l]
                l += 1
                r -= 1
            elif s[l] in vowels:
                r -= 1
            elif s[r] in vowels:
                l += 1
            else:
                l += 1
                r -= 1

        return "".join(s)