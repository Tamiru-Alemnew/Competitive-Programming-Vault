from sortedcontainers import SortedList
class MyCalendar:

    def __init__(self):
        self.booked = SortedList()
    def book(self, start: int, end: int) -> bool:
        for s , e in self.booked:
            if s <= start < e or s < end <= e :
                return False

        self.booked.add((start, end))

        return True     
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)