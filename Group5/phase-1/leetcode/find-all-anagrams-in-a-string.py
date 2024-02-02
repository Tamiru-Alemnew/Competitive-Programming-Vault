class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        left, right = 0, 0
        pdict = {}
        sdict = {}

        # Count the frequency of characters in string p
        for char in p:
            pdict[char] = pdict.get(char, 0) + 1

        while right < len(s):
            # Expand the window by adding the character at the right index
            if s[right] in sdict:
                sdict[s[right]] += 1
            else:
                sdict[s[right]] = 1

            # Shrink the window if its size exceeds the length of string p
            if right - left + 1 > len(p):
                if s[left] in sdict:
                    sdict[s[left]] -= 1
                    if sdict[s[left]] == 0:
                        del sdict[s[left]]
                left += 1

            # Compare the character frequencies in the window with the target frequencies
            if sdict == pdict:
                ans.append(left)

            right += 1

        return ans
