# Problem: Open the Lock - https://leetcode.com/problems/open-the-lock/

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        def get_next_states(state):
            next_states = []
            state_digits = list(state)
            for i in range(4):
                original_digit = state_digits[i]

                state_digits[i] = '9' if original_digit == '0' else str(int(original_digit) - 1)
                next_states.append(''.join(state_digits))
                state_digits[i] = '0' if original_digit == '9' else str(int(original_digit) + 1)
                next_states.append(''.join(state_digits))
                
                state_digits[i] = original_digit
            return next_states

        def bfs():
            queue = deque(["0000"])
            visited = set(["0000"])
            turn = 1 
            while queue:
                for _ in range(len(queue)):
                    current = queue.popleft()
                    for neighbour in get_next_states(current):
                        if neighbour not in visited and neighbour not in deadend:
                            if neighbour == target:
                                return turn

                            queue.append(neighbour)
                            visited.add(neighbour)

                turn += 1

            return -1

        if target == '0000':
            return 0
        
        deadend = set(deadends)        
        if '0000' in deadend:
            return -1

        return bfs()


        