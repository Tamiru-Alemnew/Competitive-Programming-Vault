class Solution:
    def sortSentence(self, s: str) -> str:
        s = list(s.split())
        def comparator(word):
            return int(word[-1])

        s.sort(key = comparator)
        ans = []
        for l in s:
            ans.append(l[:-1])

        return " ".join(ans)


        