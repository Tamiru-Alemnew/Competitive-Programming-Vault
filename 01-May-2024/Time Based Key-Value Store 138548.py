# Problem: Time Based Key-Value Store - https://leetcode.com/problems/time-based-key-value-store/

class TimeMap:

    def __init__(self):
        self.keyValue = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyValue[key].append((timestamp , value))

    def get(self, key: str, timestamp: int) -> str:

        time_stamps = self.keyValue[key]

        ind = bisect_right(time_stamps , (timestamp , chr(127)))

        return time_stamps[ind-1][1] if ind else ""


        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)