# Problem: Alien Dictionary ( GeeksforGeeks ) - https://www.geeksforgeeks.org/problems/alien-dictionary/1

from collections import defaultdict, deque

class Solution:
    def findOrder(self,alien_dict, N, K):
    # code here
        charcter = set()
        graph = defaultdict(list)
        inorder = defaultdict(int)
        
        for i in range(N - 1):
            word1, word2 = alien_dict[i], alien_dict[i + 1]
            l = min(len(word1), len(word2))
            
            for i in range(l):
                if word1[i] != word2[i]:
                    graph[word1[i]].append(word2[i])
                    inorder[word2[i]] += 1
                    break
                    
            
            charcter.update(word1)
            charcter.update(word2)
            
        q = deque()
        
        for ch in charcter:
            if ch not in inorder:
                q.append(ch)
               
                
        result = []
        while q:
            node = q.popleft()
            result.append(node)

            for nbr in graph[node]:
                inorder[nbr] -= 1
                if inorder[nbr] == 0:
                    q.append(nbr)
                           
                            
        return result