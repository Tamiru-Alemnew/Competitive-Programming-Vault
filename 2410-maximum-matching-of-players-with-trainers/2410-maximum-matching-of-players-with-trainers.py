class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        trainers.sort()
        players.sort()
        j,i,count = 0,0,0
        
        for j in range(len(trainers)):
            if len(players)>i and players[i] <= trainers[j]:
                count += 1
                i+=1

        return count
        