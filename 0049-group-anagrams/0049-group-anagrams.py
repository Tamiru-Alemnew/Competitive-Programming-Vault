class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:   
        rept = {}

        for w in strs:  
            if "".join(sorted(w)) not in rept:
                rept["".join(sorted(w))] = []

            rept["".join(sorted(w))] .append(w)

        ans = list(rept.values())

        return ans
