# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        Trie = {}
        def insert(word):
            root = Trie

            for char in word:
                if char not in root:
                    root[char] = {}
                root = root[char]
                
        def check(word):
            root = Trie
            ans = []
            for char in word :
                if char == "1":
                    if "0" in root:
                        ans.append("1")
                        root = root["0"]
                    else:
                        ans.append("0")
                        root = root["1"]
                else:
                    if "1" in root:
                        ans.append("1")
                        root = root["1"]
                    else:
                        ans.append("0")
                        root = root["0"]

            return int("".join(ans) , 2)

        for n in nums:
            seg = ["0"]*32
            cur = bin(n)   
            i = 32 - len(cur) + 2
            seg[i:] = list(cur[2:])
            insert(seg)

        result = 0     

        for n in nums:
            seg = ["0"]*32
            cur = bin(n)   
            i = 32 - len(cur) + 2
            seg[i:] = list(cur[2:])
            temp = check(seg)
            result  = max(temp, result)


        return result