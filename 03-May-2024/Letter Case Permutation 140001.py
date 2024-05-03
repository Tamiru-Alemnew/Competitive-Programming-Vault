# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        letters = []
        for i , c in enumerate(s):
            if not c.isdigit():
                letters.append(i)

        answer = []

        for mask in range(1<<len(letters)):
            current = list(s)

            for i in range(len(letters)):
                if 1<<i & mask :
                    current[letters[i]] = current[letters[i]].upper()
                else: 
                    current[letters[i]] = current[letters[i]].lower()

            answer.append("".join(current))

        return answer

        
