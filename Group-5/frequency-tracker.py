class FrequencyTracker:

    def __init__(self):
        self.arr = []
        self.freq = defaultdict(int)
        self.freqOffreq =  defaultdict(int)
    def add(self, number: int) -> None:
        self.arr.append(number)
        self.freqOffreq[self.freq[number]] -= 1
        self.freq[number] += 1 
        self.freqOffreq[self.freq[number]] += 1
    def deleteOne(self, number: int) -> None:
        if self.freq[number]:
            self.freqOffreq[self.freq[number]] -= 1
            self.freq[number] -= 1 
            self.freqOffreq[self.freq[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:   
        return  self.freqOffreq[frequency]
            



# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)