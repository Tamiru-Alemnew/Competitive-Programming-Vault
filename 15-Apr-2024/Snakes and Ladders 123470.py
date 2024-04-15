# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        def get_square_coordinates(square_number):
            row, col = (square_number - 1) // board_size, (square_number - 1) % board_size
            
            if row % 2 == 1:
                col = board_size - 1 - col
            
            return board_size - 1 - row, col

        board_size = len(board)  
        queue = deque([1]) 
        visited = {1}  
        steps = 0 

        while queue:
            
            for _ in range(len(queue)):
                current_square = queue.popleft()

                if current_square == board_size * board_size:
                    return steps

                for next_square in range(current_square + 1, min(current_square + 7, board_size * board_size + 1)):
                    i, j = get_square_coordinates(next_square)

                    if board[i][j] != -1:
                        next_square = board[i][j]

                    if next_square not in visited:
                        queue.append(next_square)
                        visited.add(next_square)

            steps += 1
      
        return -1