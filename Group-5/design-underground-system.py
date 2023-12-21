class UndergroundSystem:

    def __init__(self):
        self.travel = {}
        self.average = defaultdict(list)
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.travel[id] = [stationName,t]
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        journeyKey = (self.travel[id][0] , stationName)
        self.average[journeyKey].append(t-self.travel[id][1])
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.average[startStation ,endStation])/len(self.average[startStation ,endStation])
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)