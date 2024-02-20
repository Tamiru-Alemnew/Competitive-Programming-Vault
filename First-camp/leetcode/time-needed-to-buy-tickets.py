class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        queue = deque(range(n))
        time_taken = 0
        
        while tickets[k] > 0:
            front_person = queue.popleft()
            if tickets[front_person] > 0:
                tickets[front_person] -= 1
                time_taken += 1
                if front_person == k and tickets[k] == 0:
                    return time_taken
            queue.append(front_person)