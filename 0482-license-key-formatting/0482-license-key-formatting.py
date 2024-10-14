class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        removeDash = s.split("-")
        normalized = "".join(removeDash)

        group = len(normalized) // k
        first = len(normalized) % k 

        result = []
        init = []
        for i in range(first):
            if not normalized[i].isdigit():
                init.append(normalized[i].upper())
            else:
                init.append(normalized[i])
        if init :
            result.append("".join(init) )
        cur = first 
        while group > 0 :
            init = []
            for i in range(k):
                if not normalized[i+cur].isdigit():
                    init.append(normalized[i+cur].upper())
                else:
                    init.append(normalized[i+cur])

            result.append("".join(init) )
            group -= 1
            cur += k 

        return "-".join(result)




