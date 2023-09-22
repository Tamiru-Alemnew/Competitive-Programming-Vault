class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:   
        rept = {}

        for w in strs:
            sorted_w = "".join(sorted(w)) 
            if sorted_w not in rept:
                rept[sorted_w] = []

            rept[sorted_w] .append(w)

        ans = list(rept.values())

        return ans
