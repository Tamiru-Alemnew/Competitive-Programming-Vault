class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ps = [0]*(n+2)
        for s , e , seat in bookings:
            ps[s] += seat
            ps[e+1] -= seat

        for i in range(1,n+1):
            ps[i] += ps[i-1]

        return ps[1:-1]

        