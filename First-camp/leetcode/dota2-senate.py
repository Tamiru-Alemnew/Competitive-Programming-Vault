class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        count = Counter(senate)
        que = deque(list(senate))
        
        R = count["R"] #Number of Radiants currently active
        D = count["D"] #Number of Dire currently active

        removeD = 0 #lost Dire but still in the queue
        removeR = 0 #lost radiants still in the queue

        while que :
            cur = que.popleft()
            if cur == "R" :
                #if lost radients are in queue, simply pop them and decrease
                if removeR :
                    removeR -= 1
                else :
                    #increment lost dire to be removed from the queue
                    removeD += 1
                    #active dire
                    D -= 1
                    if D <= 0 :
                        return "Radiant"
                    que.append(cur)
            else :
                if removeD :
                    removeD -= 1
                else :
                    removeR += 1
                    R -= 1
                    if R <= 0 :
                        return "Dire"
                    que.append(cur)
        


        