class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1="qwertyuiop"
        row2="asdfghjkl"
        row3="zxcvbnm"
        res=[]
        for word in words:
            w=word.lower()
            if len(set(row1+w))==len(row1) or len(set(row2+w))==len(row2) or len(set(row3+w))==len(row3) :
                res.append(word)
        return res