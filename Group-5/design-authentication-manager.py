class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.time = timeToLive 
        self.token = defaultdict(int)     
    def generate(self, tokenId: str, currentTime: int) -> None:
        self.token[tokenId] = currentTime
    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.token and  currentTime - self.token[tokenId] < self.time:
            self.token[tokenId] = currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0 
        
        for  val in self.token.values():
            if currentTime - val < self.time :
                count +=1 
        return count
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)